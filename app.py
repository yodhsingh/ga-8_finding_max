from streamlit import title, header, subheader, write, number_input

title('Maximum of three numbers')
header("Enter three numbers")
subheader("in the boxes below")
a = number_input("Number 1:")
b = number_input("Number 2:")
c = number_input("Number 3:")

write("**Maximum** _value_ :")
write(max(a,b,c))
