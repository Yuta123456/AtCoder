h_1, m_1, h_2, m_2, k = map(int, input().split())
time = h_1 * 60 + m_1
print(h_2 * 60 + m_2 - time - k)