<template>
  <div class="example-block">
    <el-select v-model="addBiliUpNmae" filterable placeholder="Select">
      <el-option
        v-for="item in article"
        :key="item.Bili_up_name"
        :value="item.Bili_up_name"
      />
    </el-select>
  </div>
  <div>
    <p v-text="article"></p>
    <el-button @click="getArticle">请求</el-button>
  </div>
  <h2>登陆</h2>
  <div>
    <el-input v-model="l.username" placeholder="Name" style="width: 200px" />
    <el-input
      v-model="l.password"
      placeholder="Password"
      style="width: 200px"
    />
    <el-button @click="doLogin">登陆</el-button>
  </div>
  <h2>修改</h2>
  <div>
    <el-input v-model="a.title" placeholder="Title" style="width: 200px" />
    <el-input v-model="a.author" placeholder="Author" style="width: 200px" />
    <el-input v-model="a.body" placeholder="Body" style="width: 200px" />
    <el-button @click="postArticle">Post</el-button>
  </div>
  <div>
    <el-input v-model="pnum" placeholder="Num" style="width: 200px" />
    <el-input v-model="b.title" placeholder="Title" style="width: 200px" />
    <el-input v-model="b.author" placeholder="Author" style="width: 200px" />
    <el-input v-model="b.body" placeholder="Body" style="width: 200px" />
    <el-button @click="putArticle">Put</el-button>
  </div>
  <div>
    <el-input
      v-model="dnum.Bili_follow_name"
      placeholder="Num"
      style="width: 200px"
    />
    <el-button @click="delArticle">Del</el-button>
  </div>
</template>
<script lang="ts" >
import axios from "axios";
import qs from "qs";
axios.defaults.withCredentials = true;
export default {
  data() {
    return {
      l: {
        username: "",
        password: "",
      },
      value: "",
      options: [{ value: "123" }, { value: "2" }, { value: "3" }],
      article: "233",
      pnum: "",
      dnum: { Bili_follow_name: "多罗西123" },
      a: {
        title: "",
        author: "",
        body: "",
      },
      b: {
        title: "",
        author: "",
        body: "",
      },
      c: {
        title: "",
        author: "",
        body: "",
      },
      follow: {
        // oldpassword: "111",
        newpassword: "hhhh1234",
      },
    };
  },
  methods: {
    getArticle() {
      axios
        .get("http://127.0.0.1:8000/api/isRoot")
        .then((response) => {
          // handle response
          this.article = response.data;
          console.log("查询ing");
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        });
    },
    doLogin() {
      if (this.l.username == "") {
        alert("用户名不能为空");
        return false;
      }
      if (this.l.password == "") {
        alert("密码名不能为空");
        return false;
      }
      axios
        .post("http://127.0.0.1:8000/api/login", this.l)
        .then((res) => {
          console.log(res);
          if (res.data.status == 200) {
            alert("登陆成功");
            console.log(res);
            // this.$store.commit("setToken", res.data);
            localStorage.userName = this.l.username;
            localStorage.token_expire = res.data.expire;
            localStorage.token = res.data.token;
            this.$notify({
              title: "提示信息",
              message: "登录成功",
              type: "success",
            });
            this.$router.push({ path: "/test" });
          } else {
            this.$notify({
              title: "提示信息",
              message: "账号或密码错误",
              type: "error",
            });
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    login() {
      console.log(this.l);
      axios
        .post("http://127.0.0.1:8000/api/login/", this.l)
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    postArticle() {
      axios
        .post("http://127.0.0.1:8000/api/chpasswd/", this.follow)
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });
    },

    putArticle() {
      console.log(qs.stringify(this.a));
      axios
        .put("http://127.0.0.1:8000/api/articles/" + this.pnum, this.b)
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    delArticle() {
      console.log(qs.stringify(this.a));
      axios
        .delete("http://127.0.0.1:8000/api/weibo/followlist/", {
          data: this.dnum.Bili_follow_name,
        })
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>