import vk_api


def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    upload = vk_api.VkUpload(vk_session)
    upload.photo(['static/img/map.jpg', 'static/img/map.png'], album_id=ALBUM_ID, group_id=GROUP_ID)

    if __name__ == '__main__':
        main()
