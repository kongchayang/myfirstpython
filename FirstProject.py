# Set our bye_count to sero, no one has said anything yet...
bye_count = 0
while bye_count < 3:
# Inital condition is set to True
    should_run = True

# Use the that condition as part of the 'while'
    while should_run:
        user_input= input("What?")
        print("%s" % (user_input,))
        if user_input== "bye":
        should_run == False

        bye_count = bye_count + 1

# Reassing bye_count using it's previous value
        print(bye_count)


