<template>
  <div class="login clearfix">
    <div class="login-wrap" id="minlg">
      <el-row type="flex" justify="center">
        <el-form ref="loginForm" :model="user" status-icon label-width="80px">
          <h3>注册</h3>
          <hr />
          <el-form-item prop="username" label="用户名">
            <el-input
              v-model="user.username"
              placeholder="请输入用户名"
            ></el-input>
          </el-form-item>
          <el-form-item prop="password" label="密码">
            <el-input
              v-model="user.password"
              show-password
              placeholder="请输入密码"
            ></el-input>
          </el-form-item>
          <el-form-item prop="password" label="密码">
            <el-input
              v-model="user.passwordtwo"
              show-password
              placeholder="请再次输入密码"
            ></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" icon @click="doRegister()"
              >注册账号</el-button
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
        passwordtwo: "",
      },
    };
  },
  created() {
    // console.log($);
    // console.log("1111");
  },
  methods: {
    doRegister() {
      if (!this.user.username) {
        this.$message.error("请输入用户名！");
        return;
      } else if (!this.user.password) {
        this.$message.error("请输入密码！");
        return;
      } else if (this.user.password != this.user.passwordtwo) {
        this.$message.error("两次密码不一样！");
      } else {
        // this.$router.push({ path: "/" }); //无需向后台提交数据，方便前台调试
        axios
          .post("http://127.0.0.1:8000/api/register/", {
            username: this.user.username,
            password: this.user.password,
          })
          .then((res) => {
            console.log("输出response.data", res.data);
            // console.log("输出response.data.status", res.data.status);
            if (res.data.status) {
              localStorage.userName = res.data.user_name;
              localStorage.token = res.data.token;
              this.$router.push({ path: "/dynasic" });
            } else {
              this.$message.error(res.data.data);
            }
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
  line-height: 20px;
}

h3 {
  color: #0babeab8;
  font-size: 24px;
}
hr {
  background-color: #444;
  margin: 20px auto;
}

.el-button {
  width: 80%;
  margin-left: -50px;
}
</style>