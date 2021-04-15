import vk_api, vk
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import codecs
from datetime import date
from vk_api.longpoll import VkLongPoll, VkEventType

with open('compliment', encoding='utf-8') as f:
    compl = f.readlines()

f.close()


def main():
    vk_session = vk_api.VkApi(
        token='46aec0ebeb9e328d2676b1ba2df18671da076247942844127249910bb90cd2bea738e794f431f5554be75')
    vk = vk_session.get_api()

    longpoll = VkBotLongPoll(vk_session, 203559408)

    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Комплимент', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('Милая картиночка', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Какой сегодня праздник', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_vkpay_button(hash="action=transfer-to-group&group_id=203559408")

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            vk.messages.send(
                user_id=event.obj.message['from_id'],
                random_id=get_random_id(),
                message=':)',
                keyboard=keyboard.get_keyboard()
            )
            if event.from_user:
                if 'Ку' in str(event) or 'Привет' in str(event) or 'Хай' in str(event) or 'Хелло' in str(
                        event) or 'Хеллоу' in str(event):
                    if event.from_user:
                        vk.messages.send(
                            user_id=event.obj.message['from_id'],
                            message='Привет, милый человек :3',
                            random_id=get_random_id()
                        )

                elif 'Комплимент' in str(event):
                    if event.from_user:
                        vk.messages.send(
                            user_id=event.obj.message['from_id'],
                            random_id=get_random_id(),
                            keyboard=keyboard.get_keyboard(),
                            message=compl[random.randint(0, len(compl) - 1)]
                        )
                elif 'Милая картиночка' in str(event):
                    if event.from_user:
                        vk.messages.send(
                            user_id=event.obj.message['from_id'],
                            random_id=get_random_id(),
                            keyboard=keyboard.get_keyboard(),
                            message='Попробую отправить.....'
                        )
                        upload = vk_api.VkUpload(vk)
                        photo = upload.photo_messages(f'{random.randint(1, 6)}.jpg')
                        owner_id = photo[0]['owner_id']
                        photo_id = photo[0]['id']
                        access_key = photo[0]['access_key']
                        attachment = f'photo{owner_id}_{photo_id}_{access_key}'
                        vk.messages.send(peer_id=event.object.peer_id,
                                         user_id=event.obj.message['from_id'],
                                         random_id=get_random_id(),
                                         attachment=attachment)
                        vk.messages.send(
                            user_id=event.obj.message['from_id'],
                            random_id=get_random_id(),
                            keyboard=keyboard.get_keyboard(),
                            message='Получилось!!! Я молодец ^-^')
                elif 'Какой сегодня праздник' in str(event):
                    current_date = date.today()
                    month = current_date.month
                    day = current_date.day
                    if month < 10:
                        data = str(day) + '.0' + str(month)
                    else:
                        data = str(day) + '.' + str(month)
                    with open("C:/Users/Polina/PycharmProjects/the_best_bot_vk/holidays", encoding='utf-8') as f:
                        for line in f.readlines():
                            if data == line.split()[0]:
                                mes = ' '.join(line.split()[1:])
                                break
                        f.close()

                    if event.from_user:
                        vk.messages.send(
                            user_id=event.obj.message['from_id'],
                            random_id=get_random_id(),
                            keyboard=keyboard.get_keyboard(),
                            message=mes
                        )

                    if event.from_user:
                        vk.messages.send(
                            user_id=event.obj.message['from_id'],
                            random_id=get_random_id(),
                            keyboard=keyboard.get_keyboard(),
                            message='Поздравляю!!!!'
                        )
                else:
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message="простите, я вас не понимаю :(((",
                                     random_id=get_random_id())

if __name__ == '__main__':
    main()
