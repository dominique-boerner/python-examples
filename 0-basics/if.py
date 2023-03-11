age = 17;

# TIP: for better readability, extract the check of the if in another variable,
#      to describe, what you are checking for.
isUnderage = age < 17;

if (isUnderage):
    print("You are underaged.");
else:
    print("You are not underaged.");
