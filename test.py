import itertools
import streamlit as st

st.header("Killer Sudoku")

if "nums" not in st.session_state:
    # list(range(1, 10))  # generate numbers from 1 to 9.
    st.session_state.nums = list(range(1, 10))


def combinationSum2(*pairs):
    d = []
    for numofnums, totals in pairs:
        # generate all combinations of k digits from nums.
        combinations = itertools.combinations(st.session_state.nums, numofnums)
        # filter the combinations whose sum is equal to n.
        d.append([list(i) for i in combinations if sum(i) == totals])

    searchterms = list(itertools.product(*d))
    for counter in searchterms:
        flat_list = [num for sublist in counter for num in sublist]
        if len(set(flat_list)) == len(flat_list):
            st.write(counter)


st.write("Numbers")

col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)


def flip_num(btext, bnum):
    if st.button(btext):
        if bnum in st.session_state.nums:
            st.session_state.nums.remove(bnum)
        else:
            st.session_state.nums.insert(bnum-1, bnum)


with col1:
    flip_num("1", 1)
with col2:
    flip_num("2", 2)
with col3:
    flip_num("3", 3)
with col4:
    flip_num("4", 4)
with col5:
    flip_num("5", 5)
with col6:
    flip_num("6", 6)
with col7:
    flip_num("7", 7)
with col8:
    flip_num("8", 8)
with col9:
    flip_num("9", 9)


if st.button("Reset"):
    del st.session_state.nums
    st.session_state.nums = list(range(1, 10))  # generate numbers from 1 to 9.

st.write(st.session_state.nums)

if st.button("Run"):
    combinationSum2([3, 10], [3, 14])
