<template>

  <body>
  <div class="fullpage">
    <div class="container">

      <nav>
        <button class="menu"></button>
        <input v-on:value="this.SearchUsers" @input="Input_Username" @keyup.enter="Search_User" class="user_search" type="text" placeholder="Search">
      </nav>
      <div class="user_array">
        <Names_List v-bind:Room="Rooms"/>
      </div>
    </div>
    <div class="chat-page">

    </div>
  </div>
  </body>

</template>





<script>
import Names_List from '@/components/Names_List'
import $ from "jquery";

export default {
  components: {
    Names_List
  },
  name: 'Home_Page',

  Data() {
    return {
      Rooms: [
      ],
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
          console.log(response)
          const Da = response.data
          console.log(Da)
          while (Da.length){
            this.Rooms.push({IdRoom: Da[0]["id"], NameUser: Da[0]["invited"], Text: Da[0]["text"], LastDate: Number(Da[0]["date"].substr(0, 19).replaceAll("-","").replace("T","").replaceAll(":",""))})
            delete Da[0]
          }
        }
      })
    },

    Search_User(){
      $.ajax({
        url: "http://127.0.0.1:8000/api/v1/adduser/",
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
          alert(data.responseJSON)
          this.$router.go()
        }
      })
    },
  },

  mounted(){

    this.token = sessionStorage.getItem('AuthToken')
    this.username = sessionStorage.getItem('Username')
    if (!this.token){
      this.$router.push('components/Sign_In')
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


</style>