<template>

  <div class="user_array" v-for="Room in Rooms" v-bind:key = "Room.IdRoom">
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

</template>




<script>

export default {
  props:{
    rooms: {
      type: Array
    }
  },
  name: 'NamesList',

  Data() {
    return {

    };
  },
  methods: {}
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