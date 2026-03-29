def is_phishing(url):
    score = 0


    if not url.startswith("https://"):
        print("[WARNING] Website is not secure (no HTTPS)")
        score += 1

    if len(url) > 75:
        print("[WARNING] URL is too long")
        score += 1

    if "@" in url:
        print("[WARNING] '@' symbol found in URL")
        score += 1

    if "-" in url:
        print("[WARNING] '-' found in domain (may be fake)")
        score += 1

    suspicious_words = ["login", "verify", "update", "bank", "secure"]
    for word in suspicious_words:
        if word in url.lower():
            print(f"[WARNING] Suspicious word detected: {word}")
            score += 1

    if score >= 3:
        return "❌ Phishing Website Detected"
    else:
        return "✅ Safe Website"


def start_detector():
    print("🤖 AI Phishing Website Detector")
    print("Type 'exit' to stop\n")

    while True:
        url = input("Enter Website URL: ").strip()

        if url.lower() == "exit":
            print("Detector stopped.")
            break

        if url == "":
            print("URL cannot be empty!")
            continue

        result = is_phishing(url)
        print("Result:", result)
        print("-" * 40)


if __name__ == "__main__":
    start_detector()