"""FOL-style inference — Neha's online order eligibility."""

facts = {
    "Account(Neha)",
    "ValidPayment(Neha)",
    "DeliveryAddress(Neha)",
}

if "Account(Neha)" in facts and "ValidPayment(Neha)" in facts:
    facts.add("CanPay(Neha)")

if "CanPay(Neha)" in facts and "DeliveryAddress(Neha)" in facts:
    facts.add("CanOrder(Neha)")

if __name__ == "__main__":
    print("Can place order:", "CanOrder(Neha)" in facts)
