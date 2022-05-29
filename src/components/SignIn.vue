<template>
    <!--Основная карточка с содержимым всего поля входа-->
    <div class="form-div">
      <div class="card">

        <!--Группа кнопок входа и регистрации-->
        <p class="btn_group">
          <a class="login" text-decoration="none">
            Вход
          </a>
          <router-link class="sign_up" to="components/SignUp" >
            Регистрация
          </router-link>
        </p>

        <!--Инпуты для имени пользователя и пароля-->
        <div class="form-container">
          <p><input v-bind:value="Username" @input="Input_Username" id="username" class="form-input username" type="text" placeholder="Имя пользователя"></p>
          <p><input v-bind:value="Password" @keyup.enter="Login" @input="Input_Password" id="password" class="form-input password" type="password" placeholder="Пароль"></p>

          <!--Кнопка для отправки инфы с инпутов-->
          <div class="container_btn">
            <p class="form-buttons">
              <button v-on:click="Login" class="form-button">Войти</button>
            </p>
          </div>
        </div>
      </div>
    </div>
</template>











<script>
import $ from "jquery";


export default {
  name: 'SignIn',

  data(){
    return{
      Username: "",
      Password: "",
      Token: "",
    };
  },
  methods: {

    //авторизация
    Login() {
      $.ajax({
        url: "http://127.0.0.1:8000/auth/token/login/",
        type: "POST",
        data: {
          username: this.Username,
          password: this.Password
        },
        success: (response) => {
          this.Token = response.auth_token
          sessionStorage.setItem("AuthToken", this.Token)
          sessionStorage.setItem("Username", this.Username)
          this.$router.push('components/HomePage')


        },
        error: (data) => {
          alert(data.responseJSON.non_field_errors[0])
        }
      })
    },

    //реактивное заполнение переменной из поля ввода
    Input_Username(event) {
      this.Username = event.target.value;
    },

    //реактивное заполнение переменной из поля ввода
    Input_Password(event) {
      this.Password = event.target.value;
    },
  },

  //Во время перехода отчищаются сессионные переменные
  mounted() {
    sessionStorage.setItem('AuthToken', "")
    sessionStorage.setItem('Username', "")
    sessionStorage.setItem('ChoiceName', "")
    sessionStorage.setItem('IdRoomChoice', "")
  }
}
</script>















<style scoped>


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
.btn_group{
  display: flex;
  width: 16rem;
}
.login{
  border-radius: 2rem 0 0 2rem;
  text-align: center;
  background-color: rgb(158, 158, 255);
  height: 1.6rem;
  color: #fff;
  padding-top: .25rem;
  width: 8rem;
}


.sign_up{
  border-radius: 0 2rem 2rem 0;
  text-align: center;
  background-color: #fff;
  height: 1.5rem;
  color: rgb(158, 158, 255);
  border: #fff .05rem solid;
  padding-top: .25rem;
  width: 8rem;
  text-decoration: none;
  transition-duration: .5s;
  cursor: pointer;
}
.sign_up:hover{
  border: rgb(158, 158, 255) .05rem solid;
  box-shadow:inset 0rem 0rem .325rem rgb(158, 158, 255);
}
.form-button{
  width: 100%;
  display: block;
  position: relative;
  cursor: pointer;
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
  background-color: transparent;
  color: rgb(158, 158, 255);
  border: rgb(158, 158, 255) .05rem solid;
  font-family: fantasy;
  padding: .15rem 2rem;
  border-radius: 25px;
  font-size: 1.25rem;
  transition-duration: .5s;
  cursor: pointer;
}
.form-button:hover{
  box-shadow: 0rem 0rem .5rem rgb(158, 158, 255);
  color: rgb(89, 160, 44);
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
