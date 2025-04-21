import streamlit as st

# Custom CSS
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg,rgb(9, 122, 221),#cfe2f3);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(204, 229, 15, 0.93);
        color: black;
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: black;
    }
    .stButton>button {
        background: linear-gradient(45deg,#0b5394, #351c75);
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0, 200, 255, 0.23);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, rgba(80, 235, 32, 0.76), rgba(201, 5, 222, 0.89));
        color: black;
    }
    .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: rgba(255,255,255,0.1);
        padding: 20px;
        border-radius: 10px;
        margin: 20px;
        box-shadow: 0px 5px 15px rgba(0,201,255,0.3);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<h1>Unit Converter using Python and Streamlit</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight, and temperature.")

# Sidebar
conversion_type = st.sidebar.selectbox("Choose the conversion type", ["length", "weight", "temperature"])
value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

# Dropdowns
if conversion_type == "length":
    length_units = ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "inch", "foot"]
    with col1:
        from_unit = st.selectbox("From", length_units)
    with col2:
        to_unit = st.selectbox("To", length_units)
elif conversion_type == "weight":
    weight_units = ["kilogram", "gram", "milligram", "pound", "ounce"]
    with col1:
        from_unit = st.selectbox("From", weight_units)
    with col2:
        to_unit = st.selectbox("To", weight_units)
else:  # temperature
    temp_units = ["celsius", "fahrenheit", "kelvin"]
    with col1:
        from_unit = st.selectbox("From", temp_units)
    with col2:
        to_unit = st.selectbox("To", temp_units)

# Conversion functions
def length_converter(value, from_unit, to_unit):
    units = {
        "meter": 1, "kilometer": 1000, "centimeter": 0.01,
        "millimeter": 0.001, "mile": 1609.34, "yard": 0.9144,
        "foot": 0.3048, "inch": 0.0254
    }
    return value * units[from_unit] / units[to_unit]

def weight_converter(value, from_unit, to_unit):
    units = {
        "kilogram": 1, "gram": 0.001, "milligram": 0.000001,
        "pound": 0.453592, "ounce": 0.0283495
    }
    return value * units[from_unit] / units[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "celsius":
        return value * 9/5 + 32 if to_unit == "fahrenheit" else value + 273.15
    elif from_unit == "fahrenheit":
        return (value - 32) * 5/9 if to_unit == "celsius" else (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin":
        return value - 273.15 if to_unit == "celsius" else (value - 273.15) * 9/5 + 32

# Button & result
if st.button("🔄 Convert"):
    if conversion_type == "length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "weight":
        result = weight_converter(value, from_unit, to_unit)
    else:
        result = temperature_converter(value, from_unit, to_unit)

    st.markdown(
        f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>",
        unsafe_allow_html=True
    )

st.markdown("<div class='footer'>Created with ❤️ by Namra Khawaja Ashraf</div>", unsafe_allow_html=True)



  

