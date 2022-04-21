<template>
  <b-form @submit="login">
    <!--Основная карточка с содержимым всего поля входа-->
    <div class="form-div">
      <div class="card">

        <!--Группа кнопок входа и регистрации-->
        <p class="btn_group">
          <a class="btn login" text-decoration="none">
            Вход
          </a>
            <router-link to="components/Sign_Up">
              <a class="btn sign_up" text-decoration="none">
                Регистрация
              </a>
            </router-link>
        </p>

        <!--Инпуты для имени пользователя и пароля-->
        <div class="form-container">
          <p><input v-bind:value="username" @input="inputUsername" id="username" class="form-input username" type="text" placeholder="Имя пользователя"></p>
          <p><input v-bind:value="password" @keyup.enter="login()" @input="inputPassword" id="password" class="form-input password" type="password" placeholder="Пароль"></p>

          <!--Кнопка для отправки инфы с инпутов-->
          <div class="container_btn">
            <p class="form-buttons">
              <button v-on:click="login" class="form-button">Войти</button>
            </p>
          </div>
        </div>
      </div>
    </div>
  </b-form>
</template>











<script>
import $ from "jquery";


export default {
  name: 'Sign_In',

  Data(){
    return{
      username: "",
      password: "",
      token: "",
    };
  },
  methods: {
    login() {
      //логика авторицации

      $.ajax({
        url: "http://127.0.0.1:8000/auth/token/login/",
        type: "POST",
        data: {
          username: this.username,
          password: this.password
        },
        success: (response) => {
          console.log(response)
          this.token = response.auth_token
          sessionStorage.setItem("auth_token", response.auth_token)
          this.$router.push('components/Home_Page')


        },
        error: (data) => {
          console.log(this.password)
          alert(data.responseJSON.non_field_errors[0])
        }
      })
    },
  inputUsername(event) {
    this.username = event.target.value;
  },
  inputPassword(event) {
    this.password = event.target.value;
  },
}
}
</script>















<style scoped>

.form-button:hover{
  background-color: lightskyblue;
}

.card{
  background-color: #fff;
  box-shadow: 0 0 1rem 0 rgba(0,0,0,.2);
  display:flex;
  max-width: 300px;
  flex-direction: column;
  margin: 5.5rem auto 12.5rem;;
  border-radius: 10px;
  align-items: center;
  position: relative;
  opacity: 0;
  transition: 1.5s;
  animation: show 1s 1;
  animation-fill-mode: forwards;
}
@keyframes show{
  0%{
    opacity: 0;
  }
  100%{
    margin-top: 7.5rem;
    opacity: 1;
  }
}
.form-container{
  display: flex;
  flex-direction: column;
  align-items: center;
}
.btn{
  display: inline-block;
  font-weight: 400;
  line-height: 1.5;
  text-align: center;
  vertical-align: middle;
  font-size: 1rem;
  color: blue;
  background-color: #fff;
  border-color: blue;
  margin-right: 0;
  margin-left: 0;
  padding-left: .2rem;
  padding-right: .375rem;
  cursor: pointer;
  padding-top: .2rem;

}
.btn_group{
  display: inline-flex;
}
.login{
  border-radius: 25px 0 0 25px;
  text-align: center;

}

.login:hover{
  color: #fff;
}

.sign_up{
  border-radius: 0 25px 25px 0;
  color: blue;
  background-color: #fff;
  border-color: blue;
  text-decoration: none;
  vertical-align: middle;
  font-size: 1rem;
  padding-right: .3rem;
  padding-left: .25rem;
  font-family:Arial, Helvetica, sans-serif;
  text-align: center;
}

.login,.sign_up:hover{
  color: #fff;
  background-color: blue;
}
.form-button{
  width: 100%;
  display: block;
  position: relative;
}
.form-input{
  border-radius: 2px;
  border: 2px solid #E9F2FF;
  font-size: 14px;

  height: 1.5rem;
  width: 100%;
}
.form-button{
  right: 0;
  top: 0;
  border: 1px solid transparent;
  background-color: blue;
  color: #fff;
  font-family: fantasy;
  padding: .15rem 2rem;
  border-radius: 25px;
  font-size: 1.25rem;
}
.container_btn{
  display: flex;
  justify-content: space-between;
}

.username{
  background: url("../img/avatar.svg") no-repeat;
  background-size: 1.5rem;
  padding-left: 1.6rem;
  width: 10rem;
  font-size: 15px;
}
.password{
  background: url("../img/key.svg") no-repeat left;
  background-size: 1.5rem;
  padding-left: 1.6rem;
  width: 10rem;
}

</style>
