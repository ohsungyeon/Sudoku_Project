import streamlit as st
from sudoku import generate_puzzle

st.set_page_config(page_title="Sudoku Game", page_icon="🧩")

st.title("🧩 Sudoku Game")

if "puzzle" not in st.session_state:
    puzzle, solution = generate_puzzle(empty_count=40)
    st.session_state.puzzle = puzzle
    st.session_state.solution = solution
    st.session_state.user_board = [row[:] for row in puzzle]

if st.button("새 게임 시작"):
    puzzle, solution = generate_puzzle(empty_count=40)
    st.session_state.puzzle = puzzle
    st.session_state.solution = solution
    st.session_state.user_board = [row[:] for row in puzzle]
    st.rerun()

st.write("빈칸에 숫자를 입력하세요.")

for r in range(9):
    cols = st.columns(9)

    for c in range(9):
        if st.session_state.puzzle[r][c] != 0:
            cols[c].text_input(
                label=f"{r}-{c}",
                value=str(st.session_state.puzzle[r][c]),
                disabled=True,
                label_visibility="collapsed"
            )
        else:
            value = cols[c].text_input(
                label=f"{r}-{c}",
                value="",
                max_chars=1,
                label_visibility="collapsed"
            )

            if value.isdigit() and 1 <= int(value) <= 9:
                st.session_state.user_board[r][c] = int(value)
            else:
                st.session_state.user_board[r][c] = 0

if st.button("정답 확인"):
    if st.session_state.user_board == st.session_state.solution:
        st.success("정답입니다! 🎉")
    else:
        st.error("아직 정답이 아닙니다.")

if st.button("정답 보기"):
    st.write("정답 보드")
    st.table(st.session_state.solution)