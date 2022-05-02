<template>

  <div class="user_array">
    <div class="user_array">
      <ul class="user_ul">
        <li class="user_info" v-for="Room in Rooms" v-bind:key = "Room.IdRoom">
          <div class="user_li" @click="Choice(Room.NameUser, Room.IdRoom)">
            <div class="avatar_image">
              <img class="avatar_photo" src="../img/avatar.svg" alt="#">
            </div>
            <div class="username">
              <p class="group_user_date">
                <span class="username_info" >{{Room.NameUser}}</span>
                <span class="last_messege_date">{{Room.Time}}</span>
              </p>
              <p class="draft">
                <span class="last-messege_info">{{Room.Text}}</span>
                <span class="unread marker"></span>
              </p>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>

</template>




<script>

export default {
  props:{
    Rooms: {
      type: Array
    }
  },
  name: 'NamesList',

  data() {
    return {

    };
  },
  methods: {
    Choice(NameChoice, IdRoomChoice){
      sessionStorage.setItem("ChoiceName", NameChoice)
      sessionStorage.setItem("IdRoomChoice", IdRoomChoice)

    }
  }
}


</script>




<style scoped>
body{
  margin: 0;
  padding: 0;
  font-family: Arial, Helvetica, sans-serif;
  background: url("../img/1639788469_27-catherineasquithgallery-com-p-rozovii-fon-minimalistichnii-71.jpg");
  background-size: cover;

}
p{
  margin: 0;
  padding: 0;
}

/*Блок всей страницы*/
.fullpage{
  display: flex;
  flex-wrap: wrap;
  min-width: 100vh;
  min-height: 100vh;
  flex-direction: row;
  overflow: hidden;
}

/*Левая часть (поиск, список пользователей)*/
.container{
  background-color: #fff;
  box-shadow: 0 0 1rem 0 rgba(0,0,0,.2);
  height: inherit;
  width: 25%;
  overflow: hidden;
  display: flex;
  flex-direction: column;

}
/*Навигационная панель с менюшкой и поиском*/
nav{
  align-items: center;
  position: center;
  justify-content: space-between;
  display: flex;
  vertical-align: middle;
  padding-left: 1rem;
  padding-right: 1rem;
  font-size: 20px;
  max-width: 100%;
  min-height: 3.5rem;
}
/*Кнопка-меню*/
.menu{
  background-image: url("../img/menu-svgrepo-com.svg");
  background-color: transparent;
  background-repeat: no-repeat;
  background-position: calc(1.5rem - 1.75rem / 2) calc(1.5rem - 1.75rem / 2);
  background-size: 1.75rem;
  border-radius: 25px;
  min-height: 3rem;
  min-width: 3rem;
  border: transparent;
  margin-right: .5rem;
}
.menu:hover{
  background-color: rgb(240, 240, 240);
}
/*Поиск пользователя из списка*/
.user_search{
  display: flex;
  border-radius: 20px;
  border: 1px solid rgb(160, 160, 160);
  background-image: url("../img/icons8-search.svg");
  background-position-x: calc(2.2rem / 2 - .75rem);
  background-position-y: calc(2.5rem / 2 - 1rem);
  margin-right: .5rem;
  padding-left: 2.5rem;
  font-size: 18px;
  background-size: 2rem;
  min-height: 2.5rem;
  width: 100%;
  background-repeat: no-repeat;
}

/*Контейнер списка пользователей*/
.user_array{
  padding-left: 1rem;
  min-height: 90%;
}

/*Список пользователей*/
.user_ul{
  height: 90vh;
  overflow: auto;
  overflow-x: hidden;
  margin: 0rem;
  padding-left: .5rem;
}

/*Элемент списка*/
.user_li{
  margin-right: 1rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  height: 4rem;
  padding-left: .3rem;
  border-radius: 15px;
  transition-duration: .25s;

}
.user_li:hover{
  background-color: rgb(235, 235, 235);
  border-radius: 15px;
}

/*Содержимое элемента*/
.group_user_date{
  max-width: calc(100% - 3.6rem);
  display: flex;
  justify-content: space-between;
  margin-top: 0rem;
  margin-bottom: 1rem;
}
.avatar_image{
  margin-right: 1rem;
  min-width: 2.5rem;
  min-height: 2.5rem;
}
.username{
  display: flex;
  flex-wrap: wrap;
  max-width: 100%;
  max-height: 3rem;
}
.username_info{
  font-family: "Arial Rounded MT Bold";
  display: flex;
  width: 30rem;
}
.last_messege_date{
  display: flex;
}
.draft{
  margin-top: 0;
}

::-webkit-scrollbar {
  width: 0;
  height: 0;
}

.user_ul{
  scrollbar-width: thin;
  scrollbar-color: grey;
}

/*Правая часть с чатом и инфой*/
.chat-page{
  display: flex;
  flex-direction: column;
  min-height: 100%;
  visibility: visible;
  width: 75%;
}

/*Информация касаемо пользователя, блок сверху*/
.chat-info{
  flex: 1 1 auto;
  background-color: #fff;
  display: inline-flex;
  flex-direction: row;
  height: 3.5rem;
  padding-top: .2rem;
  padding-left: 2rem;
  border-left: 1px solid grey;
  box-shadow: 0px 1px 5px -1px rgba(0,0,0,.21);
}
.online_or_not{
  margin-top: .2rem;
}
.chat-username{
  margin-top: .3rem;
}
.chat-avatar{
  max-width: 3rem;
  max-height: 3rem;
  margin: .25rem;
}
.search-button{
  border-radius: 25px;
  height: 3rem;
  width: 3rem;
  background-size: 2rem;
  margin-top: .25rem;
  border: transparent;
  margin-right: .5rem;
  background-color: #fff;
  background-image: url("../img/icons8-search.svg");
  background-repeat: no-repeat;
  background-position: .5rem .5rem;
}
.three-dots-button{
  border-radius: 25px;
  height: 3rem;
  width: 3rem;
  background-size: 2.2rem;
  margin-top: .25rem;
  border: transparent;
  margin-right: .5rem;
  background-color: #fff;
  background-image: url("../img/three-dots.svg");
  background-repeat: no-repeat;
  background-position: .4rem .4rem;
}
.search-button:hover, .three-dots-button:hover{
  background-color: rgba(224, 224, 224, 0.637);
}
.chat-panel{
  display: flex;
  justify-content: space-between;
  flex: 1 1 auto;
  z-index: 1000;
}

/*Основная область чата*/
.chat{
  display: flex;
  align-items: center;
  flex-direction: column;
  height: 90vh;
  width: 100%;
  justify-content: flex-end;
  z-index: -1;
}

/*Внешний контейнер чата*/
.out-chat-window{
  display: flex;
  align-items: center;
  justify-content: space-around;
}
/*Основной контейнер чата*/
.chat-window{
  display: flex;
  max-width: 60%;
  min-height: 100%;
  padding-left: 1rem;
  padding-right: 1rem;
  flex-direction: column-reverse;
  justify-content: flex-start;
  scrollbar-width: none;
  scrollbar-color: grey;
  overflow-y: auto;
}
/*Строка чата*/
.chat-row{
  display: flex;
  margin-top: 1rem;
  margin-bottom: 1rem;
  flex-wrap: wrap;

}
/*Классы guest и host находятся вместе с классом chat-row и отвечают за то,
к какой стороне прикрелено сообщение */
.guest{
  justify-content: flex-start;
}
.host{
  justify-content: flex-end;
}
/*Оформление сообщений*/
.host-messege, .guest-messege{
  background-color: #fff;
  border-radius: 10px;
  box-shadow:  0 .5rem .5rem 0 rgba(0,0,0,.2);
  display: inline-flex;
  padding: 1rem;
  max-width: 50%;
  flex-direction: column;
}
.time-send-row{
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  justify-content: space-between;
  opacity: 50%;
  font-size: 13px;
}
/*Цвета сообщений*/
.host-messege{
  background-color: rgb(235, 235, 235);
}
.guest-messege{
  background-color: rgb(250, 218, 221);
}

/*Блок ввода сообщений*/
.chat-input{
  min-height: 3rem;
  min-width: 60%;
  padding-right: 1.25rem;
  display: flex;
  align-items: center;
  padding-top: .5rem;
  padding-bottom: 1.5rem;
}
.input{
  margin: .3rem;
  padding-left: 1rem;
  border: transparent;
  border-radius: 5px;
  box-shadow: 0 .5rem .5rem 0 rgba(0,0,0,.2);
  min-height: 100%;
  min-width: 100%;
}
</style>