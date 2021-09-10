import streamlit as st

from moviequotes.quote import get_quote

"Hello, World"

response, author = get_quote()

f"{response} - {author}"
