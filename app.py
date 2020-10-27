import streamlit as st
import pandas as pd
from psycopg2 import connect, extensions, sql

# declare a new PostgreSQL connection object
try:
    conn = connect(
        dbname="data_sci",
        user="postgres",
        host="localhost",
        password="postgres"
    )
    print("Database connected")
    print("\ntype(conn):", type(conn))
except:
    print("Unable to connect to database")

# @st.cache(allow_output_mutation=True)
def get_data():
    # Define queries
    # sql_command = "SELECT * FROM {}.{};".format(str(schema), str(table))
    # queries_map = {
    #     "temperature": [QUERY_TEMPERATURE, NAMES_TO_CODES[state]],
    #     "pollution": [QUERY_POLLUTION, state],
    #     "precipitations": [QUERY_PRCP, NAMES_TO_CODES[state]],
    # }
    #
    # queries_fetchers = [
    #     DataQuery(name, queries_map[name][0], queries_map[name][1], year)
    #     for name in queries_map
    # ]
    #
    # results = run_concurrent_queries(queries_fetchers)

    # return results
    sql_query = """
            SELECT * FROM company_divisions LIMIT 10;
            """
    df = pd.read_sql(sql_query, con=conn)
    return df



# This is the main app which appears when the user selects "Run the app".
def run_the_app():
    # To make Streamlit fast, st.cache allows us to reuse computation across runs.
    # Here we load latitude/longitude only once
    # @st.cache
    # def load_lat_log(file):
    #     return pd.read_csv(file, sep=";")

    # In the sidebar, the user select a state and a year and hit run
    # state_name, year = frame_selector_ui()

    # Draw an altair chart for the map
    # xy_states = load_lat_log("data/xy_states.csv")
    # Map plot are not updated, problem from streamlit
    # data = xy_states[xy_states.state == state_name[0]][['latitude', 'longitude']]
    # st.write(data)

    # ATTENTION: NOT WORKING PROPERLY
    # Github issue: https://github.com/streamlit/streamlit/issues/475
    # For now, showing the map of the US only

    # st.deck_gl_chart(
    #     viewport={"latitude": 42.0682, "longitude": -96.7420, "zoom": 3, "pitch": 40}
    # )

    mode = st.sidebar.radio("Analytics Platform",
                            ["Google Analytics",
                             "Airbnb",
                             "Instagram",
                             "Mailchimp"
            ])
    if mode == "Google Analytics":
        df = get_data()
        st.dataframe(df)
    st.markdown("Made with ♡ ")


def main():
    # Render the readme as markdown using st.markdown.
    # readme_text = st.markdown(get_file_content_as_string("instructions.md"))

    # Add a selector for the app mode on the sidebar.
    st.sidebar.title("Good Weekend")
    st.sidebar.subheader(("Navigation"))

    app_mode = st.sidebar.radio(
        "Choose the app mode", ["Show instructions", "Run the app"]
    )
    #conn = get_database_connection()

    if app_mode == "Show instructions":
         st.sidebar.success('To continue select "Run the app".')
    elif app_mode == "Run the app":
    #     readme_text.empty()
         run_the_app()


if __name__=="__main__":
    main()