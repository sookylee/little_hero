from announcement.models import Post


# data type must be dictionary
def push_data(data) : 
    temp = Post.objects.get(regist_no = data['regist_no'])
    ## update
    if temp and temp.recruit_status != data['recruit_status'] :
        temp.recruit_status = data['recruit_status']
        print(data +' has updated.')
    ## push
    else : 
        Post(
                regist_no = data['regist_no'],
                title = data['title'],
                recruit_status = data['recruit_status'],
                adult_status = data['adult_status'],
                domain = data['domain'],
                text = data['text'],
                do_date = data['do_date'],
                do_time = data['do_time'],
                do_week = data['do_week'],
                recruit_date = data['recruit_date'],
                recruit_member = data['recruit_member'],
                recruit_company = data['recruit_company'],
                telephone = data['telephone'],
                address_city = data['address_city'],
                address_gu = data['address_gu'],
                address_remainder = data['address_remainder'],
                url = data['url']
            ).save()
        print(data +' has pushed.')

