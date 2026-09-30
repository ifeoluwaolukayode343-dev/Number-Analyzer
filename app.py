import streamlit as st

def calculate_sum(numbers):
    return sum(numbers)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def find_largest(numbers):
    return max(numbers)

def find_smallest(numbers):
    return min(numbers)

def get_even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]

def get_odd_numbers(numbers):
    return [number for number in numbers if number % 2 != 0]




# ----------------
# Streamlit App
# ----------------


st.set_page_config(
    page_title="Number Analyzer",
    page_icon="🔢",
    layout="centered"
)

# -------------------------
# Gradient background and styling
# -------------------------

st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg,
        #0f2027,
        #203a43,
        #2c5364
    );
}

h1 {
    color: white;
    text-align: center;
}

p, label {
    color: white !important;
}

.stTextInput > div > div > input {
    background-color: rgba(255, 255, 255, 0.12);
    color: white;
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 8px;
}

.stButton > button {
    width: 100%;
    border-radius: 8px;
    background-color: rgba(255, 255, 255, 0.15);
    color: white;
    border: 1px solid rgba(255, 255, 255, 0.4);
}

.stButton > button:hover {
    background-color: rgba(255, 255, 255, 0.25);
    color: white;
}

.result-box {
    padding: 15px;
    margin-top: 15px;
    border-radius: 10px;
    background-color: rgba(255, 255, 255, 0.12);
    border: 1px solid rgba(255, 255, 255, 0.25);
}
</style>
""", unsafe_allow_html=True)

st.title("🔢 Number Analyzer")
st.text("Enter a list of numbers and let the app analyze them.")

# User input
user_input = st.text_input(
    "Enter numbers seperated by commas:",
    placeholder="Example: 1, 2, 3, 4..."
)

if st.button("Analyze"):

    if user_input.strip() == "":
        st.warning("Please enter some numbers.")

    else:
        try:
            # Convert the user's input into a list of numbers
            numbers = [
                float(number.strip())
                for number in user_input.split(",")

            ]

            if len(numbers) == 0:
                st.warning("Please enter at least one number.")


            else:
                st.success("Numbers analyzed successfully!")


                # -------------------
                # Your Numbers
                # -------------------

                st.subheader("📋 Your Numbers")

                # ------------------------------
                # Display the list as plain text
                # ------------------------------
                numbers_display = ", ".join(
                    str(number) for number in numbers
                    )
                st.write(numbers_display)


                # ---------------------
                # Performance Analysis
                # ---------------------

                total = calculate_sum(numbers)
                average = calculate_average(numbers)
                largest = find_largest(numbers)
                smallest = find_smallest(numbers)
                even_numbers = get_even_numbers(numbers)
                odd_numbers = get_odd_numbers(numbers)



                # ----------------
                # Analysis Results
                # ----------------


                st.subheader("📊 Analysis Results")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric("Total", total)
                    st.metric("Largest Number", largest)
                    st.metric("Number of Values", len(numbers))


                with col2:
                    st.metric("Average", round(average, 2))
                    st.metric("Smallest Number", smallest)

                # ------------
                # Even Numbers
                # ------------

                st.subheader("🔵 Even Numbers")
                if even_numbers:


                    even_display = ", ".join(
                        str(number) for number in even_numbers
                    )

                    st.text(even_display)


                else:
                    st.text("No even numbers found.")


                # --------------
                # Odd Numbers
                # --------------

                st.subheader("🟠 Odd Numbers")
                if odd_numbers:


                    odd_display = ", ".join(
                        str(number).rstrip("0").rstrip(".")
                        if "." in str(number)
                        else str(number)
                        for number in odd_numbers
                    )

                    st.markdown(odd_display)

                else:
                    st.markdown("No odd numbers found.")

        except ValueError:
             st.error(
                "Invalid input. Please enter numbers seperated by commas."
            )


    # Footer
    st.divider()
    st.caption(
        "Number Analyzer | Built with Python and Streamlit | 𝕴~𝕶𝕺𝕯🪷"
               )