<template>
  <div class="chat-window">
  <section class="chat-row host">
    <div class="guest-messege">
      <span>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatem, assumenda.</span>
      <p class="time-send-row">
        <span></span>
        <span class="time-send">15:48</span>
      </p>
    </div>
  </section>
  </div>

</template>



<script>



</script>




<style scoped>

.time-send-row{
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  justify-content: space-between;
  opacity: 50%;
  font-size: 13px;
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

/*Основной контейнер чата*/
.chat-window{
  min-height: 100%;
  padding-left: 1rem;
  padding-right: 1rem;
  display: inline-flex;
  flex-direction: column-reverse;
  justify-content: flex-start;
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
  flex-wrap: wrap;

}

.host{
  justify-content: flex-end;
}

.guest-messege{
  background-color: rgb(250, 218, 221);
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

/*Основной контейнер чата*/
.chat-window{
  min-height: 100%;
  max-width: 60%;
  display: flex;
  flex-direction: column-reverse;
  justify-content: flex-start;
  scrollbar-width: none;
  scrollbar-color: grey;
  overflow-y: auto;
}
/*Строка чата*/
.chat-row{
  min-width: 100%;
  display: flex;
  margin-top: 1rem;
  margin-bottom: 1rem;
}

.host{
  justify-content: flex-end;
}

.guest-messege{
  background-color: rgb(250, 218, 221);
}

</style>
