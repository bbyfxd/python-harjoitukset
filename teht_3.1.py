#Write a program that asks a fisher the length of a zander in centimeters.
# If the zander does not fulfill the size limit,
# the program instructs to release the fish back into the lake and notifies the user
# of how many centimeters below the size limit the caught fish was.
# A zander must be 42 centimeters or longer to meet the size limit.

kuhan_pituus = input("Anna kuhan pituuden (cm):")

if kuhan_pituus >= str(42):
    print("Ok")
elif kuhan_pituus < str(42):
    print("Release back")
    print("It's,",42-int(kuhan_pituus),"cm under the limit.")

