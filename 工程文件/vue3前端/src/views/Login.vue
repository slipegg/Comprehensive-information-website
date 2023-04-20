<template>
  <div class="login" clearfix>
    <div class="login-wrap" id="minlg">
      <el-row type="flex" justify="center">
        <el-form
          ref="loginForm"
          :model="user"
          :rules="rules"
          status-icon
          label-width="80px"
        >
          <h3>登录</h3>
          <hr />
          <el-form-item prop="username" label="用户名">
            <el-input
              v-model="user.username"
              placeholder="请输入用户名"
              prefix-icon
            ></el-input>
          </el-form-item>
          <el-form-item id="password" prop="password" label="密码">
            <el-input
              v-model="user.password"
              show-password
              placeholder="请输入密码"
            ></el-input>
          </el-form-item>
          <router-link to="/">找回密码</router-link>
          &nbsp;
          <router-link to="/register">注册账号</router-link>
          <el-form-item>
            <el-button type="primary" id="logButton" @click="doLogin()"
              >登 录</el-button
            >
          </el-form-item>
        </el-form>
      </el-row>
    </div>
  </div>
</template>
 
<script>
import axios from "axios";
export default {
  name: "login",
  data() {
    return {
      user: {
        username: "",
        password: "",
      },
    };
  },
  created() {},
  methods: {
    doLogin() {
      if (!this.user.username) {
        this.$message.error("请输入用户名！");
        return;
      } else if (!this.user.password) {
        this.$message.error("请输入密码！");
        return;
      } else {
        //校验用户名和密码是否正确;
        // this.$router.push({ path: "/personal" });
        // this.$router.push({ path: "/hot" });
        console.log("this.user:", this.user);
        axios
          .post("http://127.0.0.1:8000/api/login/", this.user)
          .then((res) => {
            // console.log("输出response.data.status", res.data.status);
            if (res.data.status === 200) {
              localStorage.userName = res.data.user_name;
              localStorage.token = res.data.token;
              // localStorage.token_expire = res.data.expire;
              // localStorage.isLogin = true;
              this.$router.push({ path: "/dynasic" });
            } else {
              this.$message.error(res.data.data);
            }
          })
          .catch((err) => {
            this.$message.error("您输入的用户名或密码错误！");
          });
      }
    },
  },
};
</script>
 
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#minlg {
  width: 400px;
  background: rgba(197, 194, 183, 0.572);
}
#logButton {
  position: relative;
  left: 30px;
  width: 90px;
}
.login {
  /* width: 1920px;*/
  height: 740px;
  background: url("../assets/login2.jpg") no-repeat;
  /* background-size: cover; */
  background-size: 100% 100%;
  overflow: hidden;
  /* background-size: contain;
  border: 1px solid black; */
}
.login-wrap {
  /* background: url("../assets/images/login_bg.png") no-repeat; */
  background-size: cover;
  width: 400px;
  height: 300px;
  margin: 215px auto;
  overflow: hidden;
  padding-top: 10px;
  line-height: 40px;
}
#password {
  margin-bottom: 5px;
}
h3 {
  color: #0babeab8;
  font-size: 24px;
}
hr {
  background-color: #444;
  margin: 20px auto;
}
a {
  text-decoration: none;
  color: rgb(131, 127, 127);
  font-size: 15px;
}
a:hover {
  color: coral;
}
.el-button {
  width: 80%;
  margin-left: -50px;
}
</style>