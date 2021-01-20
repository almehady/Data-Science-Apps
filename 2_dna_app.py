import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('dna.jpg')
st.image(image, use_column_width=True)
st.write(
    """
    # DNA Nucleotide Count Web App
    This app counts nucleotide composition of query DNA!
    """
)
st.header('Enter DNA Seqence')
sequence_input = ">DNA Query\n GATCGGGGGGGTTTTAACCTTCCCCTTTGGGTTTAAACCGATCGGGGGGGTTTTAAAACCCCGGGTTTAAACCCC"
sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # skips the first line
sequence = ''.join(sequence) # concatenates list of strings

def DNA_nucleotide_count(seq):
  d = dict([
            ('A',seq.count('A')),
            ('T',seq.count('T')),
            ('G',seq.count('G')),
            ('C',seq.count('C'))
            ])
  return d

X = DNA_nucleotide_count(sequence)

st.subheader('Display as Dataframe')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

st.subheader('Display Bar Chart Using Altair')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
).properties(
    width=alt.Step(80)
)
st.write(p)