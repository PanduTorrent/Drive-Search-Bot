from telegraph import Telegraph

telegraph = Telegraph()
telegraph.create_account(short_name=input("Enter a username for your Telegra.ph :FREAKHEAD"))

print(f"Your Telegra.ph token ==>  {telegraph.get_access_token(10679e9976d1451a1650fe45197df8d4ae166037fd17e9f828d14c272750)}")
