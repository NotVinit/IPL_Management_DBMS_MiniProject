import streamlit as st
import mysql.connector
import pandas as pd

# Connect to MySQL database
def connect_to_database():
    return mysql.connector.connect(
        host='localhost',
        user='VinitNotFound',
        password='jayjalaram',
        database='IPLManagement'
    )

# Function to insert data into Players table
def insert_player_data(player_data):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        # Execute SQL insert statement
        cursor.execute("INSERT INTO Players (PlayerName, Age, TeamId, IPLDebut, Specialization, MatchesPlayed, PlayingStyle, Nationality) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", player_data)

        # Commit changes
        connection.commit()
        st.success("Player data inserted successfully")

    except mysql.connector.Error as error:
        st.error(f"Failed to insert player data: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def fetch_column_names_players():
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        # Execute SQL query to fetch column names
        cursor.execute("SHOW COLUMNS FROM Players")

        # Fetch all rows
        columns_data = cursor.fetchall()

        # Extract column names
        column_names = [column[0] for column in columns_data]
        return column_names

    except mysql.connector.Error as error:
        print(f"Failed to fetch column names for Players table: {error}")
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to fetch all records from the Players table
def fetch_all_players():
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM players")
        players_data = cursor.fetchall()
        return players_data
    except mysql.connector.Error as error:
        st.error(f"Failed to fetch venues data: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def delete_player_by_id(player_id):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM venues WHERE PlayerID = %s", (player_id,))

        connection.commit()


    except mysql.connector.Error as error:
        print(f"Failed to delete player: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
