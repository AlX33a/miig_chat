<template>

  <div class="chat-info">
    <img class="chat-avatar" src="../img/avatar.svg" alt="#">
    <div class="chat-panel">
      <div class="user_info_text">
        <p class="chat-username">{{Username}}</p>
        <p class="online_or_not">{{online}}</p>
      </div>
      <div class="nav-btn">
        <button class="search-button"></button>
        <button class="three-dots-button"></button>
      </div>
    </div>
  </div>

</template>



<script>



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

::-webkit-scrollbar {
  width: 0;
  height: 0;
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
  box-shadow: 0 1px 5px -1px rgba(0,0,0,.21);
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

::-webkit-scrollbar {
  width: 0;
  height: 0;
}

/*Информация касаемо пользователя, блок сверху*/
.chat-info{
  background-color: #fff;
  display: inline-flex;
  flex-direction: row;
  min-width: 100%;
  height: 3.5rem;
  padding-left: 2rem;
  border-left: 1px solid grey;
  box-shadow: 0 1px 5px -1px rgba(0,0,0,.21);
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
  width: 90%;
}

</style>
