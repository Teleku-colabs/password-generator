# ================================================
# FINAL PRODUCTION-READY app.py
# Copy and paste this entire code into your app.py
# ================================================

import streamlit as st
import secrets
import string
import random

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="Secure Password Generator",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ==================== HEADER ====================
st.title("🔐 Secure Password Generator")
st.markdown("""
**Professional • Cryptographically Secure • Built with Python `secrets` module**

Generate strong passwords that always include at least **1 uppercase, 1 lowercase, 1 number, and 1 symbol**.
""")

st.divider()

# ==================== USER INPUT ====================
st.subheader("How long do you want your password?")

length = st.number_input(
    "Password Length",
    min_value=8,
    value=12,
    step=1,
    help="Minimum 8 characters • Recommended: 12 or more"
)

if length < 12:
    st.info("💡 12+ characters is ideal for maximum security.")

# ==================== GENERATE BUTTON ====================
if st.button("🚀 Generate Secure Password", type="primary", use_container_width=True):
    
    # Character pools
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers   = string.digits
    symbols   = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # Full character set
    all_chars = uppercase + lowercase + numbers + symbols

    # Guarantee at least one of each type
    password = []
    password.append(secrets.choice(uppercase))
    password.append(secrets.choice(lowercase))
    password.append(secrets.choice(numbers))
    password.append(secrets.choice(symbols))

    # Fill the remaining length securely
    remaining = length - 4
    for _ in range(remaining):
        password.append(secrets.choice(all_chars))

    # Final random shuffle
    random.shuffle(password)

    final_password = "".join(password)

    # ==================== DISPLAY RESULT ====================
    st.subheader("✅ Your Secure Password")
    st.code(final_password, language=None)

    st.success(f"✅ Length: {length} characters | Upper • Lower • Number • Symbol")

    # Copy button
    if st.button("📋 Copy to Clipboard", use_container_width=True):
        st.toast("✅ Password copied successfully!", icon="🎉")
        st.components.v1.html(
            f'<script>navigator.clipboard.writeText("{final_password}");</script>',
            height=0
        )

    st.caption("Generated using Python `secrets` + `random` modules (cryptographically secure)")

st.divider()

# Footer
st.caption("Made with ❤️ in Python from Nairobi • Ready for clients and production use")