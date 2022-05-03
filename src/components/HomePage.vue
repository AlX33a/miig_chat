<template>

  <body>
  <div class="fullpage">
    <div class="container">

      <nav>
        <button class="menu"></button>
        <input v-on:value="this.SearchUsers" @input="Input_Username" @keyup.enter="Search_User" class="user_search" type="text" placeholder="Search">
      </nav>
      <NamesList v-bind:Rooms="Rooms"/>
    </div>
    <div class="chat-page">
      <div class="chat-info">
        <img class="chat-avatar" src="../img/avatar.svg" alt="#">
        <div class="chat-panel">
          <div class="user_info_text">
            <p class="chat-username">{{ChoiceName}}</p>
          </div>
          <div class="nav-btn">
            <button class="logout-button" @click="Go_Sign_In"></button>
          </div>
        </div>
      </div>
      <div class="chat" v-show="!visible">
        <div class="out-chat-window">
          <div v-for="Message in Messages" v-bind:key = "Message.LastDate">
            <section class="chat-row guest" v-if="Message.Name===Username">
              <div class="host-messege">
                <span>{{Message.Text}}</span>
                <p class="time-send-row">
                  <span></span>
                  <span class="time-send">{{Message.Time}}</span>
                </p>
              </div>
            </section>
            <section class="chat-row host" v-else>
              <div class="guest-messege">
                <span>{{Message.Text}}</span>
                <p class="time-send-row">
                  <span></span>
                  <span class="time-send">{{Message.Time}}</span>
                </p>
              </div>
            </section>
          </div>
        </div>
        <div class="chat-input">
          <input v-on:value="this.Message" @input="Input_Message" @keyup.enter="New_Message" class="input" type="text" placeholder="Напишите что нибудь" >
        </div>
      </div>
    </div>

  </div>
  </body>

</template>





<script>
import NamesList from '@/components/NamesList'
import $ from "jquery";

export default {
  components: {
    NamesList
  },
  name: 'HomePage',


  data() {
    return {
      Rooms: [],
      Messages: [],
      Token: "",
      Username: "",
      SearchUsers: "",
      ChoiceName: "",
      IdRoomChoice: "",
      visible: true,
      Message: "",
    };
  },


  methods: {

    ready() {
      window.setInterval(() => {
        this.Update_Rooms();
        if (this.ChoiceName!==""){
          this.Update_Message()
          this.visible = false
        }
        console.log("1")
      },5000);
    },

    Input_Username(event) {
      this.SearchUsers = event.target.value;
    },

    Input_Message(event){
      this.Message = event.target.value;
    },


    New_Message(){
      if (this.Message.length>499){
        alert("Длина сообщения не может превышать 499 символов. Ваше сообщение - " + this.Message.length)
      }else {
        $.ajax({
          url: "http://127.0.0.1:8000/api/v1/chat/",
          type: "POST",
          headers: {'Authorization': "Token " + sessionStorage.getItem('AuthToken')},
          data: {
            message: this.Message,
            dialogue: this.IdRoomChoice,
          },
          success: () => {
            this.Message = ""
            this.$router.go()
          },
          error: (data) => {
            alert(data.responseJSON.data)
          }
        })
      }
    },

    Update_Rooms(){
      $.ajax({
        url: "http://127.0.0.1:8000/api/v1/room/",
        type: "GET",
        headers: {'Authorization': "Token " + sessionStorage.getItem('AuthToken')},
        success: (response) => {
          const Da = response.data
          this.Rooms = []
          for (let i = 0; i<Da.length; i++){
            this.Rooms.push({IdRoom: Da[i]["id"], NameUser: Da[i]["invited"], Text: Da[i]["message"], LastDate: Number(Da[i]["date"].substr(0, 19).replaceAll("-","").replace("T","").replaceAll(":","")), Time: Da[i]["date"].substr(11, 2)+":"+Da[i]["date"].substr(14, 2)})
          }
          this.Rooms.sort((prev, next) => next.LastDate - prev.LastDate)
        }
      })
    },

    Search_User(){
      $.ajax({
        url: "http://127.0.0.1:8000/api/v1/room/",
        type: "POST",
        headers: {'Authorization': "Token " + sessionStorage.getItem('AuthToken')},
        data: {
          user: this.SearchUsers,
        },
        success: () => {
          this.SearchUsers = ""
          this.$router.go()
        },
        error: (data) => {
          alert(data.responseJSON.data)
          this.SearchUsers = ""
          this.$router.go()
        }
      })
    },

    Update_Message(){
      $.ajax({
        url: "http://127.0.0.1:8000/api/v1/chat/",
        type: "GET",
        headers: {'Authorization': "Token " + sessionStorage.getItem('AuthToken')},
        data: {
          dialogue: this.IdRoomChoice,
        },
        success: (response) => {
          const Da = response.data
          this.Messages = []
          for (let i = 0; i<Da.length; i++){
            this.Messages.push({Name: Da[i]["user"], Text: Da[i]["message"], LastDate: Number(Da[i]["date"].substr(0, 19).replaceAll("-","").replace("T","").replaceAll(":","")), Time: Da[i]["date"].substr(8, 2)+"."+Da[i]["date"].substr(5, 2)+"."+Da[i]["date"].substr(0, 2)+" "+Da[i]["date"].substr(11, 2)+":"+Da[i]["date"].substr(14, 2)})
          }
          this.Messages.sort((prev, next) => prev.LastDate - next.LastDate)
          console.log(this.Messages)
        }
      })
    },

    Go_Sign_In(){
      this.$router.push('components/SignIn')
    }
  },

  mounted(){

    this.Token = sessionStorage.getItem('AuthToken')
    this.Username = sessionStorage.getItem('Username')
    this.ChoiceName = sessionStorage.getItem('ChoiceName')
    this.IdRoomChoice = sessionStorage.getItem('IdRoomChoice')
    console.log(sessionStorage.getItem('ChoiceName'))
    console.log(sessionStorage.getItem('IdRoomChoice'))
    if (this.ChoiceName!==""){
      this.Update_Message()
      this.visible = false
    }
    if (!this.Token){
      this.$router.push('components/SignIn')
    }
    this.Update_Rooms()
    this.ready()
  }
}

</script>





<style scoped>
body{
  margin: 0;
  padding: 0;
  font: 16px Helvetica;
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
  display: flex;
  width: 30rem;
  font-weight: bold;
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
  width: auto;
  background-color: #fff;
  display: inline-flex;
  flex-direction: row;
  height: 3.5rem;
  padding-top: .2rem;
  padding-left: 2rem;
  border-left: 1px solid grey;
  box-shadow: 0px 1px 5px -1px rgba(0,0,0,.21);
}
.chat-panel{
  display: flex;
  justify-content: space-between;
  flex: 1 1 auto;
}
.user_info_text{
  flex: 1 1 auto;
  text-align: center;
}
.chat-username{
  padding-top: 1rem;
}
.chat-avatar{
  max-width: 3rem;
  max-height: 3rem;
  margin: .25rem;
}
.logout-button{
  border-radius: 25px;
  height: 3rem;
  width: 3rem;
  background-size: 2rem;
  margin-top: .25rem;
  border: transparent;
  margin-right: .5rem;
  background-color: #fff;
  background-image: url("../img/logout-icon.svg");
  background-repeat: no-repeat;
  background-position: calc(.6rem) calc(2rem / 4);
  transition-duration: .25s;
}
.logout-button:hover{
  background-color: rgb(243, 243, 243);
}


/*Основная область чата*/
.chat{
  display: flex;
  align-items: center;
  flex-direction: column;
  max-height: 90vh;
  width: 100%;
  justify-content: flex-end;
  z-index: 1000;
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
  height: calc(90vh - 5rem);
  padding-left: 1rem;
  padding-right: 1rem;
  flex-direction: column-reverse;
  scrollbar-width: none;
  scrollbar-color: grey;
  overflow-y: auto;
  flex: 0 1 inherit;
}
/*Строка чата*/
.chat-row{
  display: flex;
  margin-top: 1rem;
  margin-bottom: 1rem;
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
  height: 3rem;
  min-width: 60%;
  padding-right: 1.25rem;
  display: flex;
  align-items: center;
  padding-top: .5rem;
  margin-bottom: 1.5rem;
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