import pandas as pd

# Dictionary to map full state names to abbreviations
state_abbreviations = {
    "ALABAMA": "AL", "ALASKA": "AK", "ARIZONA": "AZ", "ARKANSAS": "AR",
    "CALIFORNIA": "CA", "COLORADO": "CO", "CONNECTICUT": "CT", "DELAWARE": "DE",
    "FLORIDA": "FL", "GEORGIA": "GA", "HAWAII": "HI", "IDAHO": "ID",
    "ILLINOIS": "IL", "INDIANA": "IN", "IOWA": "IA", "KANSAS": "KS",
    "KENTUCKY": "KY", "LOUISIANA": "LA", "MAINE": "ME", "MARYLAND": "MD",
    "MASSACHUSETTS": "MA", "MICHIGAN": "MI", "MINNESOTA": "MN", "MISSISSIPPI": "MS",
    "MISSOURI": "MO", "MONTANA": "MT", "NEBRASKA": "NE", "NEVADA": "NV",
    "NEW HAMPSHIRE": "NH", "NEW JERSEY": "NJ", "NEW MEXICO": "NM", "NEW YORK": "NY",
    "NORTH CAROLINA": "NC", "NORTH DAKOTA": "ND", "OHIO": "OH", "OKLAHOMA": "OK",
    "OREGON": "OR", "PENNSYLVANIA": "PA", "RHODE ISLAND": "RI", "SOUTH CAROLINA": "SC",
    "SOUTH DAKOTA": "SD", "TENNESSEE": "TN", "TEXAS": "TX", "UTAH": "UT",
    "VERMONT": "VT", "VIRGINIA": "VA", "WASHINGTON": "WA", "WEST VIRGINIA": "WV",
    "WISCONSIN": "WI", "WYOMING": "WY",
}

def clean_and_categorize_states(df, location_column):
    # Function to clean and standardize state names
    def clean_state(state):
        state = state.strip().upper()
        return state_abbreviations.get(state, state)
    # Apply the function to extract and clean state names
    df['State'] = df[location_column].str.split(', ').str[-1].apply(clean_state)
    # Debugging: Print unique states
    unique_states = df['State'].unique()
    print("Unique states:", unique_states)
    # Function to categorize states into countries
    def categorize_country(state):
        if state in state_abbreviations.values():
            return 'USA'
        else:
            return 'Other'
    # Apply the function to categorize countries
    df['Country'] = df['State'].apply(categorize_country)
    # Debugging: Print unique countries
    print("Unique countries:", df['Country'].unique())
    return df