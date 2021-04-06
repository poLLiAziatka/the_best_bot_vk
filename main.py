import vk_api, vk
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
import codecs
from vk_api.longpoll import VkLongPoll, VkEventType

with open('compliment', encoding='utf-8') as f:
    compl = f.readlines()


def main():
    vk_session = vk_api.VkApi(
        token='46aec0ebeb9e328d2676b1ba2df18671da076247942844127249910bb90cd2bea738e794f431f5554be75')
    vk = vk_session.get_api()

    longpoll = VkBotLongPoll(vk_session, 203559408)

    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Комплимент', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('Милая картиночка', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Сделать картиночку', color=VkKeyboardColor.POSITIVE)
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
                            message='Я пока не умею такое делать, простите меня пожалуйста '
                        )
                elif 'Сделать картиночку' in str(event):
                    if event.from_user:
                        vk.messages.send(
                            user_id=event.obj.message['from_id'],
                            random_id=get_random_id(),
                            keyboard=keyboard.get_keyboard(),
                            message='Простите, этому я еще не научился, но обещаю скоро научусь'
                        )
                else:
                    print(event)
                    print('Новое сообщение:')
                    print('Для меня от:', event.obj.message['from_id'])
                    print('Текст:', event.obj.message['text'])
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message="простите, я вас не понимаю :(((",
                                     random_id=random.randint(0, 2 ** 64))


"""
            if event.from_chat:
                print(event)
                print('Новое сообщение:')
                print('Для меня от:', event.chat_id)
                print('Текст:', event.obj.message['text'])
                vk.messages.send(chat_id=event.chat_id,
                                 message="Вас приветствует romАЧКА:ЗЗЗ",
                                 random_id=random.randint(0, 2 ** 64))
                
            
            if 'Ку' in str(event) or 'Привет' in str(event) or 'Хай' in str(event) or 'Хелло' in str(
                    event) or 'Хеллоу' in str(event):
                if event.from_chat:
                    vk.messages.send(
                        key=('453c553ee58dec67ee27b06174723bf3d6ff61d3'),
                        server=('https://lp.vk.com/wh202300325'),
                        ts=('132'),
                        random_id=get_random_id(),
                        message='Привет!',
                        chat_id=event.chat_id
                    )
            if 'Клавиатура' in str(event):
                if event.from_chat:
                    vk.messages.send(
                        keyboard=keyboard.get_keyboard(),
                        key=('453c553ee58dec67ee27b06174723bf3d6ff61d3'),
                        server=('https://lp.vk.com/wh202300325'),
                        ts=('132'),
                        random_id=get_random_id(),
                        message='Держи',
                        chat_id=event.chat_id
                    )
"""

if __name__ == '__main__':
    main()
