# start import
from pyrogram import Client, errors
from pyrogram.enums import ChatType
from re import match, IGNORECASE, findall
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
# end import
# start Pyrogram.Client
app = Client("iphone 11 pro" , api_id = "5888972" , api_hash = "8c6c75ac3bb436c548e56e93020cb738")
scheduler = AsyncIOScheduler({'apscheduler.job_defaults.max_instances':2})
# end Pyrogram.Client
# start DB
Admins, Timerg, Timerp, Adgs, Adps, AdCHIDG, AdIDG, AdCHIDP, AdIDP = [], [], [], [], [], [], [], [], []
# end DB
# start DB creation
if Admins:
 print('The initial database is already created!')
else:
 Owner = input('Enter the first admin ID :')
 Admins.append(int(Owner))
 Adgs.append('off')
 Adps.append('off')
 Timerg.append(int('10'))
 Timerp.append(int('10'))
# end DB creation
# start Check admin id
def checkId(Admins):
    if match("(\d{9,10})", Admins):
        return True
    else:
        return False
# end Check admin id
# start Pv Robot
async def sendtopv(client, message, post):
  dialogs = app.get_dialogs()
  async for dialog in dialogs:
   if dialog.chat.type == ChatType.PRIVATE:
    try:
      await app.copy_message(chat_id=dialog.chat.id, from_chat_id=message.chat.id, message_id=post.id)
      await asyncio.sleep(15)
    except Exception as error:
      pass
async def addgroup(client, idgap):
  dialogs = app.get_dialogs()
  async for dialog in dialogs:
   if dialog.chat.type == ChatType.PRIVATE:
    try:
      await app.add_chat_members(idgap, dialog.chat.id)
      await asyncio.sleep(10)
    except Exception as error:
      pass
async def bannerP_handler():
    if not (Adps[0] == "on"):
        return

    async for dialog in app.get_dialogs():
        if dialog.chat.type == ChatType.PRIVATE:
            try:
                await app.copy_message(chat_id=dialog.chat.id, from_chat_id=AdCHIDP[0],
                                          message_id=AdIDP[0])
                await asyncio.sleep(20)
            except (errors.FloodWait, errors.ChatWriteForbidden, errors.PeerIdInvalid, errors.MessageNotModified):
                pass
            except Exception as error:
                pass
# end Pv Robot
# start Group Robot
async def sendtogroup(client, message, post):
  dialogs = app.get_dialogs()
  async for dialog in dialogs:
   if dialog.chat.type in [ChatType.SUPERGROUP, ChatType.GROUP]:
    try:
      await app.copy_message(chat_id=dialog.chat.id, from_chat_id=message.chat.id, message_id=post.id)
      await asyncio.sleep(15)
    except (errors.FloodWait, errors.ChatWriteForbidden, errors.PeerIdInvalid, errors.MessageNotModified):
        pass
    except (errors.ChatRestricted, errors.UserBannedInChannel):
        await app.leave_chat(dialog.chat.id, delete=True)
    except (errors.ChatRestricted, errors.UserMuteedInChannel):
        await app.leave_chat(dialog.chat.id, delete=True)
    except Exception as error:
        pass
async def bannerG_handler():
    if not (Adgs[0] == "on"):
        return

    async for dialog in app.get_dialogs():
        if dialog.chat.type in [ChatType.SUPERGROUP, ChatType.GROUP]:
            try:
                await app.copy_message(chat_id=dialog.chat.id, from_chat_id=AdCHIDG[0],
                                          message_id=AdIDG[0])
                await asyncio.sleep(20)
            except (errors.FloodWait, errors.ChatWriteForbidden, errors.PeerIdInvalid, errors.MessageNotModified):
                pass
            except (errors.ChatRestricted, errors.UserBannedInChannel):
                await app.leave_chat(dialog.chat.id, delete=True)
            except (errors.ChatRestricted, errors.UserMuteedInChannel):
                await app.leave_chat(dialog.chat.id, delete=True)
            except Exception as error:
                pass
# end Group Robot
# start Panel Admin
@app.on_message()
async def user_message_handler(client, message):
    try:
        if message.from_user.id in Admins:
          if match(r'^(dns|دی ان اس)$', message.text, IGNORECASE):
            await message.reply_text("Level3 DNS\n\n4.2.2.1\n4.2.2.2\n4.2.2.3\n4.2.2.4\n\n\nOpen DNS\n208.67.222.222\n208.67.220.220\n\n\nPTE DNS\n5.202.100.100\n5.202.100.101\n5.202.129.29\n\n\nGoogle\n8.8.8.8\n8.8.4.4\n\n\nQuad9 DNS\n9.9.9.9\n149.112.112.112\n\n\nAdGuard DNS\n94.140.14.14\n94.140.15.15\n\n\nCloudflare DNS\n1.1.1.1\n1.0.0.1")
          elif match(r'^(Update|اپدیت)$', message.text, IGNORECASE):
            await message.reply_text("__Pishgaman Helper Updated__\n\nVersion:1.0.1")
          elif match(r'^(قطعی لینک|link down)$', message.text, IGNORECASE):
               await message.reply_text(f'**Click Here >>**\n\n**>** https://t.me/pishgamanHelper/3')
          elif match(r'^(تعرفه|tarefe)$', message.text, IGNORECASE):
               await message.reply_text(f'**لیست تعرفه ها**\n\n**Click Here >>**\n\nhttps://t.me/pishgamanHelper/2')
          elif match(r'^(addadmin|ادمین)$', message.text, IGNORECASE):
                admin_id = message.reply_to_message.text
                if checkId(admin_id):
                    Admins.append(int(admin_id))
                    await message.reply_text('ادمین با موفقیت اضافه شد.')
                else:
                    await message.reply_text('Added')

          elif match(r'^(Remove Admin|حذف ادمین)$', message.text, IGNORECASE):
                admin_id = message.reply_to_message.text
                if checkId(admin_id):
                    Admins.remove(int(admin_id))
                    await message.reply_text('ادمین با موفقیت حذف شد.')
                else:
                    await message.reply_text('Added')
          elif match(r'^(Join|پیوستن)$', message.text, IGNORECASE):
                    await message.reply_text('لطفا صبر کنید(لینک هایی که در آن نیازمند ارسال ریکوست است در ربات پشتیبانی نمی شود)...')
                    matches = findall("https?://(?:t\.me|telegram\.me)/\S+", message.reply_to_message.text)
                    for link in matches:

                        try:
                            await client.join_chat(link)
                            await asyncio.sleep(100)
                        except:
                            pass
                    await message.reply_text('ربات در تمامی چت ها عضو شد!')
          elif match(r'^(انتقال|ent)$', message.text, IGNORECASE):
            await message.reply_text("«انتقال اعتبار»\nدر دو مرحله خلاصه میشود\n\nامکان سنجی امکان انتقال 🅰️\n\nثبت درخواست انتقال اعتبار 🅱️\n\nدر مرحله اول خط مشترک بررسی می گردد و اگر موردی نبود ، مدارک اعلام می شود\nدر مرحله دوم بعد از تکمیل مدارک درخواست ثبت می شود\n\n-*-*-*-*-*-*-*-*-*-*-*-*-*\n\nمرحله اول 🅰️ – امکان سنجی\n\n🔰 موارد مربوط به استعلام :\nتحت پوشش باشد\nپورت آزاد وجود داشته باشد\nتوقف فروش نباشد\nاستعلام شاهکار و آسیاتک و مخابرات مثبت باشد\nخط فیبر DLC یا PCM نباشد\n\n⛔️ موارد غیر ممکن:\nانتقال از مرکز به مجتمع و\nبالعکس\nاز مجتمعی به مجتمع دیگر\nانتقال به خطی که رانژه دارد\n\n**⚠️ الزامات**\n**اطمینان از عدم وجود بدهی**\n**برقراری بوق خط شماره جدید**\n\n♻️ وضعیت پنل:\nوضعیت بهره برداری باشد (حداقل 10 روز و 5 گیگ حجم ترافیک باقی مانده)\nسرویس رزرو نداشته باشد ( اگر دارد درخواست برگشت از فروش ثبت شود)\n\n-*-*-*-*-*-*-*-*-*-*-*-*-*\nمرحله دوم🅱️:\n\nپس از تکمیل و تایید همه موارد بالا، اعلام مدارک به مشترک\n\n🔻مدارک:\nهزینه انتقال به خط جدید 132000 تومان ( اگر مجتمع هستند نیازی نیست)\nتصویر کارت ملی مالک پنل\nدرخواست دست نویس:\n– آدرس کامل\n-کد پستی\n-شماره همراه مشترک\n\nتماس برای ثبت درخواست ، از ثابت یا همراه پنل باشد\n\n✅ پس از تکمیل تمامی مراحل بالا، توضیحات تیکت شامل اطلاعات ذیل باشد و به CS تیکت نمایید\n\n📝\nباسلام\nمشترک با شماره تلفن …\nدرخواست انتقال سرویس خود به خط شماره … را دارند\nاحراز هویت صورت گرفته است\n\nو مشترک از خط ثابت/ شماره همراه خود تماس گرفته اند.\n\nتمامی موارد امکان سنجی بررسی شد و مشترک اماکن انتقال و تعویض خط را دارند\n\nشماره جدید:\nکد پستی محل جدید:\nآدرس محل:\nشماره همراه مشترک")
          elif match(r'^(Ping|ربات)$', message.text, IGNORECASE):
                await message.reply_text("**Pishgaman Helper Onlined**")
          elif match(r'^(Groups list|لیست گروه ها)$', message.text, IGNORECASE):
                number = 1
                await message.reply_text("لیست گروه هایی که ربات در آن عضو است :")
                async for group in app.get_dialogs():
                    if group.chat.type in [ChatType.SUPERGROUP, ChatType.GROUP]:
                        try:
                            await app.send_message(message.chat.id,
                                                      f"{number} - name group : {group.chat.title}\nchat id : {group.chat.id}")
                            number += 1

                            await asyncio.sleep(3)

                        except:
                            pass
                await message.reply_text("تموم شد !")
          elif match(r'^(Bot number|شماره ربات)$', message.text, IGNORECASE):
                await message.delete()
                me = await app.get_me()
                await message.reply_contact(me.phone_number, me.first_name)
          elif match(r'^(Adgroup on|تبلیغ در گروه روشن)$', message.text, IGNORECASE):
                if Adgs[0] == 'off':
                    await message.reply_text('تبلیغ در گروه فعال شد!')
                    Adgs.clear()
                    Adgs.append("on")
                else:
                    await message.reply_text('تبلیغ در گروه از قبل فعال بوده است!')
          elif match(r'^(Adgroup off|تبلیغ در گروه خاموش)$', message.text, IGNORECASE):
                if Adgs[0] == 'on':
                    await message.reply_text('تبلیغ در گروه خاموش شد!')
                    Adgs.clear()
                    Adgs.append("off")
                else:
                    await message.reply_text('تبلیغ در گروه از قبل خاموش بوده است!')
          elif match(r'^(Adpv on|تبلیغ در پیوی روشن)$', message.text, IGNORECASE):
                if Adps[0] == 'off':
                    await message.reply_text('تبلیغ در پیوی روشن شد!')
                    Adps.clear()
                    Adps.append("on")
                else:
                    await message.reply_text('تبلیغ در پیوی از قبل روشن بوده است!')
          elif match(r'^(Adpv off|تبلیغ در پیوی خاموش)$', message.text, IGNORECASE):
                if Adps[0] == 'on':
                    await message.reply_text('تبلیغ در پیوی خاموش شد!')
                    Adps.clear()
                    Adps.append("off")
                else:
                    await message.reply_text('تبلیغ درپیوی از قبل خاموش بوده است!')
          elif match(r'^(Vad group|مشاهده تبلیغ گروه)$', message.text, IGNORECASE):
              if AdIDG:
                await message.reply_text('تبلیغ کنونی گروه:')
                await client.copy_message(message.chat.id, AdCHIDG[0], AdIDG[0])
              else:
                await app.send_message(message.chat.id,
                                              'ᴇʀʀᴏʀ : \nمنن تبلیغ در گروه یافت نشد!')
          elif match(r'^(Vad pv|مشاهده تبلیغ پیوی)$', message.text, IGNORECASE):
              if AdIDP:
                await message.reply_text('تبلیغ کنونی پیوی:')
                await client.copy_message(message.chat.id, AdCHIDP[0], AdIDP[0])
              else:
                    await app.send_message(message.chat.id,
                                              'ᴇʀʀᴏʀ : \nمتن تبلیغ در پیوی یافت نشد!')
          elif message.reply_to_message:
            if match(r'^(Set ad group|تنظیم تبلیغ گروه)$', message.text, IGNORECASE):
              await app.send_message(message.chat.id,
                                              "متن (گروه) ذخیره شد.\n\n- لطفا پیام تبلیغ را پاک نکنید! ")
              AdCHIDG.clear()
              AdIDG.clear()
              AdCHIDG.append(message.chat.id)
              AdIDG.append(message.reply_to_message.id)
            elif match(r'^(Set ad pv|تنظیم تبلیغ پیوی)$', message.text, IGNORECASE):
              await app.send_message(message.chat.id,
                                              "متن (پیوی) ذخیره شد.\n\n- لطفا پیام تبلیغ را پاک نکنید! ")
              AdCHIDP.clear()
              AdIDP.clear()
              AdCHIDP.append(message.chat.id)
              AdIDP.append(message.reply_to_message.id)   
          elif match(r'^(Help|راهنما)$', message.text, IGNORECASE):
                await message.reply_text(text="""                          
**<< Pishgaman Helper >>**


❯❯ دستورات فارسی فنی:
❯ ربات - __وضیعت انلاینی ربات__
❯ `قطعی لینک` - __روال قطعی لینک__
❯ `قطعی اینترنت` - __روال قطعی اینترنت (PPPOE)__
❯ `کندی` - __روال کندی سرعت__
❯ `بریج` - __آموزش بریج__
❯ `تنظیمات` - __تنظیمات مودم__
""")
    
    
          elif match(r'^(Stats|وضعیت)$', message.text, IGNORECASE):
                await message.reply_text( f"🎛 وضعیت تبچی HxD :\n\n\n◄ تبلیغ در گروه : {Adgs[0]}\n\n◄ تبلیغ در پیوی : {Adps[0]}\n\n◄ لیست ادمین ها : {Admins}\n\n◄ تایم ارسال به گروه : {Timerg[0]}\n\n◄ تایم ارسال به پیوی : {Timerp[0]}")
    except Exception as error:
        pass

scheduler.start()
app.run()
