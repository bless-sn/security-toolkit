import tldextract
from email import policy
from email.parser import BytesParser

def analyze_url(url):
    extracted = tldextract.extract(url)

    print("Subdomain:", extracted.subdomain)
    print("Domain:", extracted.domain)
    print("Suffix:", extracted.suffix)

def score_url(url):
    extracted = tldextract.extract(url)
    score = 0
    findings = []

    risky_tlds = ["xyz", "top", "click"]

    if extracted.suffix in risky_tlds:
        score += 1
        findings.append("Risky TLD: ." + extracted.suffix)

    brands = ["paypal", "google", "amazon", "microsoft"]

    if any(brand in extracted.subdomain.lower() for brand in brands):
        score += 2
        findings.append("Brand name found in subdomain")

    return score, findings

def read_email(filename):
    with open(filename, "rb") as file:
        msg = BytesParser(policy=policy.default).parse(file)

    sender = msg.get("From", "Not provided")
    reply_to = msg.get("Reply-To", "Not provided")
    auth = msg.get("Authentication-Results", "Not provided")

    print("\n--- EMAIL ANALYSIS ---")
    print("FROM:", sender)
    print("REPLY-TO:", reply_to)
    print("AUTH:", auth)

analyze_url("https://paypal.attacker.xyz/login")

score, findings = score_url("https://paypal.attacker.xyz/login")

print("Risk Score:", score)
print("Findings:", findings)

read_email("suspicious.eml")
