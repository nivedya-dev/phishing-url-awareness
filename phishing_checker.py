import re
from urllib.parse import urlparse

def inspect_url(raw_url):
    """Check visible URL text for selected warning signs."""
    url = raw_url.strip()
    findings = []
    
    if not url:
        return ["No URL entered."]
    
    # Ensure scheme is present for parsing
    candidate = url if "://" in url else "http://" + url
    
    # Safe parsing handling malformed URLs
    try:
        parsed = urlparse(candidate)
    except ValueError:
        return ["This text is not a valid URL format."]
        
    host = (parsed.hostname or "").lower()
    
    if not host:
        return ["Could not identify a hostname."]
    
    # 1. Check for @ symbol
    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")
        
    # 2. Check for unusually long URL
    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")
        
    # 3. Check for IP address hostnames
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")
        
    # 4. Check for many subdomains/segments
    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")
        
    # 5. Check for Punycode
    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")
        
    # 6. Check for HTTP scheme
    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")
        
    if not findings:
        findings.append("No listed warning signs found. This does NOT prove safety.")
        
    return findings

def main():
    print("====================================")
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - does not open URLs")
    print("====================================\n")
    
    while True:
        raw_url = input("Enter a sample URL (or type 'q' to quit): ")
        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("Goodbye! Stay alert online.")
            break
            
        print("\nResult:")
        results = inspect_url(raw_url)
        for item in results:
            print("- " + item)
        print("Never enter passwords from unexpected links.\n")

if __name__ == "__main__":
    main()