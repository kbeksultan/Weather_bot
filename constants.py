import os
TOKEN = os.getenv("TOKEN") or os.environ.get('TOKEN')
APPID = os.getenv("APPID") or os.environ.get('APPID')

WEATHERAPI = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

cities = ['Almaty', 'Pavlodar', 'Astana',
          'Atyrau', 'Aktau', 'Semey', 'Petropavlovsk',
          'Shymkent', 'Karaganda', 'Aktobe',
          'Kyzylorda', 'Oskemen', 'Uralsk', 'Taraz']

photos = {
    "Kazakhstan": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Kazachst%C3%A1n-pah%C3%BDl-obr%C3%A1zek.svg/300px-Kazachst%C3%A1n-pah%C3%BDl-obr%C3%A1zek.svg.png",
    "Almaty": "https://astanatimes.com/wp-content/uploads/2019/11/61938cfd-fdb5-4373-bc77-bc58fbbef0c1-istock-1002496248.jpg",
    "Pavlodar": "https://www.votpusk.ru/country/ctimages/new/kz9.jpg",
    "Astana": "https://getaboutasia.com/blog/wp-content/uploads/2019/07/Astana-1.jpg",
    "Atyrau": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0d/d1/ff/26/2016.jpg?w=1000&h=-1&s=1",
    "Aktau": "https://astanatimes.com/wp-content/uploads/2017/11/akt.jpg",
    "Semey": "https://altaynews.kz/assets/cache_image/assets/image/resources/ru/2020/05/15/49685/Semey_Bridge_600x600_8a3.png",
    "Kyzylorda": "https://astanatimes.com/wp-content/uploads/2018/12/Kazpravda-3.jpg",
    "Oskemen": "https://media-cdn.tripadvisor.com/media/photo-s/18/f7/66/fe/dedeman-oskemen-tavros.jpg",
    "Uralsk": "https://photos-kr.kcdn.kz/01/2468fa0e669bf9727e5f9859d7bdfd92ee3d96/photo-448x280.jpg",
    "Taraz": "https://old.elorda.info/storage/news/1/105/70/42/21/20958/photo/big_1b893fbe65a41122.jpg",
    "Petropavlovsk": "https://cdni.rbth.com/rbthmedia/images/2017.10/article/59dcdf5915e9f9345b1d1344.jpg",
    "Shymkent": "https://www.ebrdgreencities.com/assets/Uploads/ed4092e777/Shymkent-v2__ResizedImageWzYwMCwzODRd.jpg",
    "Karaganda": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTRLYXbaSsMlUTpIa2mptfp2PwJwds7882G0g&usqp=CAU",
    "Aktobe": "https://liter.kz/wp-content/uploads/2020/06/crop_1407673427-aktobe1_1551691000-750x352.jpg"
}