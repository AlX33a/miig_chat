<template>

  <div class="user_array">
    <div class="user_array">
      <ul class="user_ul">
        <div v-for="Room in Rooms" v-bind:key = "Room.IdRoom">
          <li class="user_info" v-if="Room.User===UserName && Room.IsRead">
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
                  <span class="last-messege_info">{{"Вы: "+Room.Text}}</span>
                  <img src="../img/Logo_NIKE_green.svg" alt="#" class="marker read">
                </p>
              </div>
            </div>
          </li>
          <li class="user_info" v-else-if="Room.User===UserName && !Room.IsRead">
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
                  <span class="last-messege_info">{{"Вы: "+Room.Text}}</span>
                  <img src="../img/Logo_NIKE.svg" alt="#" class="marker unread">
                </p>
              </div>
            </div>
          </li>
          <li class="user_info" v-else-if="Room.User==='' || Room.IsRead">
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
                </p>
              </div>
            </div>
          </li>
          <li class="user_info" v-else>
            <div class="user_li_unread" @click="Choice(Room.NameUser, Room.IdRoom)">
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
                </p>
              </div>
            </div>
          </li>
        </div>
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
      UserName: sessionStorage.getItem('Username')
    };
  },
  methods: {
    //когда человек нажимает на одну из комнат - делается выбор или наоборот комната пропадает (если клиент уже в ней был)
    Choice(NameChoice, IdRoomChoice){
      if (sessionStorage.getItem('ChoiceName')!==NameChoice) {
        sessionStorage.setItem("ChoiceName", NameChoice)
        sessionStorage.setItem("IdRoomChoice", IdRoomChoice)
        this.$router.go()
      }else{
        sessionStorage.setItem("ChoiceName", "")
        sessionStorage.setItem("IdRoomChoice", "")
        this.$router.go()
      }
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
  padding-top: .2rem;
  z-index: 1;
  padding-left: 1rem;
  min-height: 90%;
  position: relative;
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
  margin-right: 1rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  height: 4rem;
  padding-left: .3rem;
  border-radius: 15px;
  transition-duration: .25s;
}
.user_li_unread{
  margin-right: 1rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  height: 4rem;
  padding-left: .3rem;
  border-radius: 15px;
  transition-duration: .25s;
  background-color:rgb(244, 244, 244);
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
  flex-direction: column;
  flex-wrap: nowrap;
  max-width: 100%;
  max-height: 3rem;
}
.username_info{
  font-weight: bold;
  display: flex;
  width: 30rem;
}
.last_messege_date{
  display: flex;
}
.draft{
  margin-top: 0;
  display: flex;
  justify-content: space-between;
  width: calc(100% - 3.6rem);
}
.marker{
  width: 1.5rem;
  height: 1.5rem;
  opacity: 100%;
}
.unread{
  display: unset;
}
.read{
  display: unset;
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