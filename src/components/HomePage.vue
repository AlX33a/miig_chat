<template>

  <body>
  <div class="fullpage">
    <div class="container">

      <nav>
        <img class="menu" src="../img/leaf.jpg">
        <input v-model="SearchUsers" @input="Input_Username" @keyup.enter="Search_User" class="user_search" type="text" placeholder="Search">
      </nav>



      <div id="search" class="search_list">

        <div class="found-users-array">
          <ul class="found-users-ul" v-for="Name in SearchUsersList" v-bind:key = "Name.Name">
            <li>
              <div class="found-user" @click="BeforeSearch(Name.Name)">
                {{Name.Name}}
              </div>
            </li>
          </ul>
        </div>


        <div class="page-manager" v-if="Quantity!==1 && Scroll!==1 && Scroll!==Quantity">
          <button class="left-arrow-btn left-green" @click="ScrollMinus"></button>
          <span class="page-counter">{{Scroll}}/{{Quantity}}</span>
          <button class="right-arrow-btn right-green" @click="ScrollPlus"></button>
        </div>
        <div class="page-manager" v-if="Quantity!==1 && Scroll===1">
          <button class="left-arrow-btn left-grey"></button>
          <span class="page-counter">{{Scroll}}/{{Quantity}}</span>
          <button class="right-arrow-btn right-green" @click="ScrollPlus"></button>
        </div>
        <div class="page-manager" v-if="Quantity!==1 && Quantity===Scroll">
          <button class="left-arrow-btn left-green" @click="ScrollMinus"></button>
          <span class="page-counter">{{Scroll}}/{{Quantity}}</span>
          <button class="right-arrow-btn right-grey"></button>
        </div>



      </div>





      <NamesList v-bind:Rooms="Rooms"/>
    </div>
    <div class="chat-page">
      <div class="chat-info">
        <img class="chat-avatar" src="../img/avatar.svg" alt="#">
        <div class="chat-panel">
          <div class="user_info_text">
            <p class="chat-username">{{ChoiceName}}</p>
            <p class="offline-p" v-if="!Online" v-show="!visible">
              <img class="online-icon" src="../img/zzz-icon.svg" alt="#">
              <span class="status offline">был в сети {{OnlineDate}}</span>
            </p>
            <p class="online-p" v-else v-show="!visible">
              <img class="online-icon" src="../img/green-circle.svg" alt="#">
              <span class="status online" >Online</span>
            </p>
          </div>
          <div class="nav-btn">
            <button class="logout-button" @click="Go_Sign_In"></button>
          </div>
        </div>
      </div>
      <div class="chat" v-show="!visible">
        <div class="out-chat-window">
          <div class="chat-window">
            <div v-for="Message in Messages" v-bind:key = "Message.LastDate">
              <section class="chat-row guest" v-if="Message.Name!==Username">
                <div class="host-messege">
                  <span class="Message-Text">{{Message.Text}}</span>
                  <p class="time-send-row">
                    <span></span>
                    <span class="time-send">{{Message.Time}}</span>
                  </p>
                </div>
              </section>
              <section class="chat-row host" v-else-if="!Message.IsRead">
                <div class="guest-messege">
                  <span class="Message-Text">{{Message.Text}}</span>
                  <p class="time-send-row">
                    <span class="time-send">{{Message.Time}}</span>
                    <img class="marker unread" src="../img/Logo_NIKE.svg" alt="#">
                  </p>
                </div>
              </section>
              <section class="chat-row host" v-else>
                <div class="guest-messege">
                  <span class="Message-Text">{{Message.Text}}</span>
                  <p class="time-send-row">
                    <span class="time-send">{{Message.Time}}</span>
                    <img class="marker read" src="../img/Logo_NIKE_green.svg" alt="#">
                  </p>
                </div>
              </section>
            </div>
          </div>
        </div>
        <div class="chat-input">
          <input v-model="Message" @input="Input_Message" @keyup.enter="New_Message" class="input" type="text" placeholder="Напишите что нибудь" >
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
      SearchUsersList: [],
      Token: "",
      Username: "",
      SearchUsers: "",
      ChoiceName: "",
      IdRoomChoice: "",
      visible: true,
      Message: "",
      Online: "",
      OnlineDate: "",
      Scroll: 1,
      Quantity: 1,
    };
  },


  methods: {
    //синхронная функция, которая обновляет сообщения и комнаты
    ready() {
      window.setInterval(() => {
            if (this.Token) {
              this.Update_Rooms();
              if (this.ChoiceName !== "") {
                this.Update_Message()
                this.visible = false
              }
            }
      },5000);
    },

    //this.SearchUsers.length>3 &&
    //Когда поле ввода заполняется - переменная получает значение мгновенно
    Input_Username(event) {
      this.SearchUsers = event.target.value;
      this.SearchUsersList=[]
      this.Scroll = 1
      this.Quantity = 1
      if (this.SearchUsers.length<13 && this.SearchUsers.length!==0){
          $.ajax({
            url: "http://127.0.0.1:8000/api/v1/search/",
            type: "GET",
            headers: {'Authorization': "Token " + sessionStorage.getItem('AuthToken')},
            data: {
              scroll: this.Scroll,
              user: this.SearchUsers,
            },
            success: (response) => {
              for (let i = 0; i<response.data.length; i++){
                this.SearchUsersList.push({Name: response.data[i]["username"]})
              }
              this.Quantity = response["quantity"]
            }
          })
      }
    },

    BeforeSearch(Name){
      this.SearchUsers = Name
      this.Scroll = 1
      this.Quantity = 1
      this.SearchUsersList = []
      this.Search_User()
    },

    //Когда поле ввода заполняется - переменная получает значение мгновенно
    Input_Message(event) {
      this.Message = event.target.value;
      this.SearchUsersList = []
      this.Scroll = 1
      this.Quantity = 1
      if (this.SearchUsers.length < 13 && this.SearchUsers.length !== 0) {
        $.ajax({
          url: "http://127.0.0.1:8000/api/v1/search/",
          type: "GET",
          headers: {'Authorization': "Token " + sessionStorage.getItem('AuthToken')},
          data: {
            scroll: this.Scroll,
            user: this.SearchUsers,
          },
          success: (response) => {
            for (let i = 0; i < response.data.length; i++) {
              this.SearchUsersList.push({Name: response.data[i]["username"]})
            }
            this.Quantity = response["quantity"]
          }
        })
      }
    },


    ScrollPlus() {
      this.Scroll = this.Scroll + 1
      this.SearchUsersList = []
      if (this.SearchUsers.length < 13 && this.SearchUsers.length !== 0) {
        $.ajax({
          url: "http://127.0.0.1:8000/api/v1/search/",
          type: "GET",
          headers: {'Authorization': "Token " + sessionStorage.getItem('AuthToken')},
          data: {
            scroll: this.Scroll,
            user: this.SearchUsers,
          },
          success: (response) => {
            for (let i = 0; i < response.data.length; i++) {
              this.SearchUsersList.push({Name: response.data[i]["username"]})
            }
            this.Quantity = response["quantity"]
          }
        })
      }
    },

    ScrollMinus(){
      this.Scroll = this.Scroll-1
      this.SearchUsersList = []
      if (this.SearchUsers.length < 13 && this.SearchUsers.length !== 0) {
        $.ajax({
          url: "http://127.0.0.1:8000/api/v1/search/",
          type: "GET",
          headers: {'Authorization': "Token " + sessionStorage.getItem('AuthToken')},
          data: {
            scroll: this.Scroll,
            user: this.SearchUsers,
          },
          success: (response) => {
            for (let i = 0; i < response.data.length; i++) {
              this.SearchUsersList.push({Name: response.data[i]["username"]})
            }
            this.Quantity = response["quantity"]
          }
        })
      }
    },

    //отправка одним пользователем сообщения
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
            if (this.Token) {
              this.Update_Rooms();
              if (this.ChoiceName !== "") {
                this.Update_Message()
                this.visible = false
              }
            }
          },
          error: (data) => {
            alert(data.responseJSON.data)
          }
        })
      }
    },


    //Обновление левого меню с комнатами
    Update_Rooms(){
      $.ajax({
        url: "http://127.0.0.1:8000/api/v1/room/",
        type: "GET",
        headers: {'Authorization': "Token " + sessionStorage.getItem('AuthToken')},
        success: (response) => {
          const Da = response.data
          this.Rooms = []
          //console.log(Da)
          for (let i = 0; i<Da.length; i++){
            this.Rooms.push({IdRoom: Da[i]["id"], NameUser: Da[i]["invited"], Text: Da[i]["message"], LastDate: Number(Da[i]["date"].substr(0, 19).replaceAll("-","").replace("T","").replaceAll(":","")), Time: Da[i]["date"].substr(11, 2)+":"+Da[i]["date"].substr(14, 2), IsRead: Da[i][["is_read"]], User: Da[i]["message_sender"]})
          }
          this.Rooms.sort((prev, next) => next.LastDate - prev.LastDate)
          //console.log(this.Rooms)
        }
      })
    },


    //Поиск пользователя
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
          if (this.Token) {
            this.Update_Rooms();
            if (this.ChoiceName !== "") {
              this.Update_Message()
              this.visible = false
            }
          }
        },
        error: (data) => {
          alert(data.responseJSON.data)
          this.SearchUsers = ""
          this.$router.go()
        }
      })
    },


    //Обномление сообщений одной комнаты
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
          this.Online = response.online.is_online
          this.OnlineDate = response.online.date
          this.Messages = []
          //console.log(response)
          for (let i = 0; i<Da.length; i++){
            this.Messages.push({Name: Da[i]["user"], Text: Da[i]["message"], LastDate: Number(Da[i]["date"].substr(0, 19).replaceAll("-","").replace("T","").replaceAll(":","")), Time: Da[i]["date"].substr(8, 2)+"."+Da[i]["date"].substr(5, 2)+"."+Da[i]["date"].substr(2, 2)+" "+Da[i]["date"].substr(11, 2)+":"+Da[i]["date"].substr(14, 2), IsRead: Da[i]["is_read"]})
          }
          this.Messages.sort((prev, next) => next.LastDate - prev.LastDate)
        }
      })
    },


    //Если сюда обращается какой-либо метод - клиента выкидывает на страницу входа
    Go_Sign_In(){
      //this.$router.go()
      $.ajax({
        url: "http://127.0.0.1:8000/auth/token/logout/",
        type: "POST",
        headers: {'Authorization': "Token " + sessionStorage.getItem('AuthToken')},
      })

      this.$router.push('components/SignIn')
    }
  },


  //Данный метод запускается при загрузке или перезагрузке страницы, запускает необходимые проверки
  mounted(){

    this.Token = sessionStorage.getItem('AuthToken')
    this.Username = sessionStorage.getItem('Username')
    this.ChoiceName = sessionStorage.getItem('ChoiceName')
    this.IdRoomChoice = sessionStorage.getItem('IdRoomChoice')
    if (this.ChoiceName!==""){
      this.Update_Message()
      this.visible = false
    }
    if (!this.Token || this.Token===''){
      //this.$router.go()
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
  height: 100vh;
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
  min-height: 3.7rem;
}
.search_list{
  background-color: #fff;
  box-shadow:  0 10px 7px -1px rgba(0,0,0,.21);
  display: flex;
  flex-direction: column;
  width: 25%;
  height: min-content;
  border-top: 1px grey solid;
  top: 3.7rem;
  z-index: 4;
  position: absolute;
  border-radius: 0 0 15px 15px;
}
.found-users-array{
  height: min-content;
}
.found-users-ul{
  list-style-type: none;
}
.found-user{
  width: 80%;
  padding-left: 1rem;
  padding-top: .5rem;
  padding-bottom: .5rem;
  border-bottom: 1px grey solid;
}
.page-manager{
  display: flex;
  justify-content: center;
  width: 100%;
  height: 3rem;
}
.left-arrow-btn{
  background-color: #fff;
  height: 2.5rem;
  width: 2.5rem;
  background-size: calc(2rem);
  background-position: 0;
  background-repeat: no-repeat;
  border-color: transparent;
  border-radius: 25px;
}
.left-green{
  background-image: url("../img/left-arrow-green.svg");
}
.left-grey{
  background-image: url("../img/left-arrow-grey.svg");
}
.right-arrow-btn{
  background-color: #fff;
  height: 2.5rem;
  width: 2.5rem;
  background-size: calc(2rem);
  background-position: 5px;
  background-repeat: no-repeat;
  border-color: transparent;
  border-radius: 25px;
}
.right-green{
  background-image: url("../img/right-arrow-green.svg");
}
.right-grey{
  background-image: url("../img/right-arrow-grey.svg");
}
.page-counter{
  margin-top: .5rem;
  margin-left: 1rem;
  margin-right: 1rem;
}
/*Кнопка-меню*/
.menu{
  background-position: -1.1rem -1rem;
  height: 4.5rem;
  width: 4.5rem;
  border-color: red;
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

::-webkit-scrollbar {
  width: 0;
  height: 0;
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
  box-shadow: 0 1px 5px -1px rgba(0,0,0,.21);
}
.chat-panel{
  display: flex;
  justify-content: space-between;
  width: 100%;
  max-height: 3.5rem;
}
.user_info_text{
  flex: 1 1 auto;
  text-align: center;
}
.chat-username{
  padding-top: calc((3.5rem) / 2 - 1.25rem);
}
.online-icon{
  height: .75rem;
  width: .75rem;
  padding-right: .2rem;
}
.status{
  font-size: 14px;
  color: rgb(92, 92, 232);
}
.offline{
  color: black;
}
.offline-p{
  opacity:50%;
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
  height: 90vh;
  width: 100%;
  justify-content: flex-end;
  z-index: 1000;
}

/*Внешний контейнер чата*/
.out-chat-window{
  display: flex;
  min-width: 100%;
  align-items: center;
  justify-content: space-around;
}
/*Основной контейнер чата*/
.chat-window{
  display: flex;
  min-width: 60%;
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
.guest-messege{
  padding-bottom: .5rem;
}
.Message-Text{
  max-width: 15rem;
  word-wrap: break-word;
}
.time-send-row{
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  opacity: 100%;
  font-size: 13px;
}
.time-send{
  opacity: 50%;
}
.marker{
  padding-top: .5rem;
  margin-left: .5rem;
  height: 1.5rem;
  width: 1.5rem;
  padding-left: 0rem;
}
.read{
  display: unset;
}
.unread{
  display: unset;
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