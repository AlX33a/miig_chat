<template>

  <body>
  <div class="fullpage">
    <div class="container">

      <nav>
        <button class="menu"></button>
        <input v-on:value="this.SearchUsers" @input="Input_Username" @keyup.enter="Search_User" class="user_search" type="text" placeholder="Search">
      </nav>
      <div class="user_array">
        <div class="user_array" v-for="Room in this.Rooms" v-bind:key = "Room.IdRoom">
          <ul class="user_ul">
            <li class="user_info">
              <div class="user_li">
                <div class="avatar_image">
                  <img class="avatar_photo" src="../img/avatar.svg" alt="#">
                </div>
                <div class="username">
                  <p class="group_user_date">
                    <span class="username_info" >{{Room.NameUser}}</span>
                    <span class="last_messege_date">#</span>
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
    </div>
    <div class="chat-page">

    </div>
  </div>
  </body>

</template>





<script>
//import NamesList from '@/components/NamesList'
import $ from "jquery";

let Roomers = [];
export default {
//  components: {
//    NamesList
//  },
  name: 'HomePage',


  Data() {
    return {
      Rooms: [],
      Token: "",
      Username: "",
      SearchUsers: "",
    };
  },
  methods: {
    Input_Username(event) {
      this.SearchUsers = event.target.value;
    },

    Update_Rooms(){
      $.ajax({
        url: "http://127.0.0.1:8000/api/v1/room/",
        type: "GET",
        headers: {'Authorization': "Token " + sessionStorage.getItem('AuthToken')},
        success: (response) => {
          const Da = response.data
          console.log(Da)
          for (let i = 0; i<Da.length; i++){
            Roomers.push({IdRoom: Da[i]["id"], NameUser: Da[i]["invited"], Text: Da[i]["text"], LastDate: Number(Da[i]["date"].substr(0, 19).replaceAll("-","").replace("T","").replaceAll(":","")), Time: Da[i]["date"].substr(11, 2)+":"+Da[i]["date"].substr(14, 2)})
          }
          this.Rooms = Roomers
          console.log(this.Rooms)
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
        success: (response) => {
          console.log(response)
          this.SearchUsers = ""
          this.$router.go()
        },
        error: (data) => {
          console.log(data)
          alert(data.responseJSON.data)
          this.$router.go()
        }
      })
    },
  },

  mounted(){

    this.token = sessionStorage.getItem('AuthToken')
    this.username = sessionStorage.getItem('Username')
    if (!this.token){
      this.$router.push('components/SignIn')
    }
    this.Update_Rooms()
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
  margin: 0;
  padding-left: .5rem;
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
  flex: 1 1 auto;
}

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
  margin: 0;
  padding-left: .5rem;
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
  min-width: 73%;
  visibility: visible;
}

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
  margin: 0;
  padding-left: .5rem;
}

/*Элемент списка*/
.user_li{
  cursor: pointer;
  display: flex;
  align-items: center;
  height: 4rem;
  padding-left: .3rem;
  margin-right: 2.2rem;
  border-radius: 15px;
  transition-duration: .25s;

}
.user_li:hover{
  background-color: rgb(235, 235, 235);
  border-radius: 15px;
}

/*Содержимое элемента*/
.group_user_date{
  max-width: 10rem;
  min-width: 100%;
  display: flex;
  justify-content: space-between;
  margin-top: 0;
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
  max-width: 10rem;
  max-height: 3rem;
}
.username_info{
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
  margin: 0;
  padding-left: .5rem;
}

/*Элемент списка*/
.user_li{
  cursor: pointer;
  display: flex;
  align-items: center;
  height: 4rem;
  padding-left: .3rem;
  margin-right: 2.2rem;
  border-radius: 15px;
  transition-duration: .25s;

}
.user_li:hover{
  background-color: rgb(235, 235, 235);
  border-radius: 15px;
}

/*Содержимое элемента*/
.group_user_date{
  max-width: 10rem;
  min-width: 100%;
  display: flex;
  justify-content: space-between;
  margin-top: 0;
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
  max-width: 10rem;
  max-height: 3rem;
}
.username_info{
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
</style>