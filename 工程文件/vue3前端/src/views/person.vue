<template>
  <el-button type="primary" id="back" @click="gotoDynasic">返回</el-button>
  <div id="bigdiv">
    <h2>{{ this.personName }},你好</h2>
    <h3>b站关注的人</h3>
    <el-table :data="biliFollowList" style="width: 100%" max-height="200">
      <el-table-column label="姓名" prop="Bili_up_name"></el-table-column>
      <el-table-column label="是否特别关注" prop="Bili_is_special">
        <template #default="scope">
          <el-select v-model="biliFollowList[scope.$index].Bili_is_special">
            <el-option label="是" value="true" />
            <el-option label="否" value="false" />
          </el-select>
        </template>
      </el-table-column>
      <el-table-column align="right">
        <template #header>
          <el-input
            v-model="search"
            size="small"
            placeholder="Type to search"
          />
        </template>
        <template #default="scope">
          <el-button
            size="small"
            type="danger"
            @click="bili_handleDelete(scope.$index)"
            >删除</el-button
          >
        </template>
      </el-table-column>
    </el-table>
    <div>
      <el-select v-model="addBiliUpName" filterable placeholder="关注的up姓名">
        <el-option
          v-for="item in BiliUpList"
          :key="item.Bili_up_name"
          :value="item.Bili_up_name"
        />
      </el-select>
      是否特别关注：
      <el-select v-model="addBiliUpIsspecial">
        <el-option label="否" value="0" />
        <el-option label="是" value="1" />
      </el-select>
      <el-button type="primary" @click="addBiliFollow">添加</el-button>
    </div>

    <h3>微博关注的人</h3>
    <el-table :data="weiboFollowList" style="width: 100%" max-height="200">
      <el-table-column label="姓名" prop="Weibo_up_name"></el-table-column>
      <el-table-column label="是否特别关注" prop="Weibo_is_special">
        <template #default="scope">
          <el-select v-model="weiboFollowList[scope.$index].Weibo_is_special">
            <el-option label="是" value="true" />
            <el-option label="否" value="false" />
          </el-select>
        </template>
      </el-table-column>
      <el-table-column align="right">
        <template #header>
          <el-input
            v-model="search"
            size="small"
            placeholder="Type to search"
          />
        </template>
        <template #default="scope">
          <el-button
            size="small"
            type="danger"
            @click="weibo_handleDelete(scope.$index)"
            >删除</el-button
          >
        </template>
      </el-table-column>
    </el-table>
    <div>
      <el-select
        v-model="addWeiboUpName"
        filterable
        placeholder="关注的博主姓名"
      >
        <el-option
          v-for="item in WeiboUpList"
          :key="item.Weibo_up_name"
          :value="item.Weibo_up_name"
        />
      </el-select>
      是否特别关注：
      <el-select v-model="addWeiboUpIsspecial">
        <el-option label="否" value="0" />
        <el-option label="是" value="1" />
      </el-select>
      <el-button type="primary" @click="addWeiboFollow">添加</el-button>
    </div>
    <h3>修改用户名</h3>
    <el-input v-model="newname" placeholder="新用户名" style="width: 200px" />
    <br />
    <el-button type="primary" @click="changename">确认修改</el-button>
    <h3>修改密码</h3>
    <span>新密码</span>

    <el-input
      v-model="password"
      show-password
      placeholder="Password"
      style="width: 200px"
    />
    <br />
    <span>再次输入新密码</span>
    <el-input
      v-model="passwordtwo"
      show-password
      placeholder="Password"
      style="width: 200px"
    />
    <br />
    <el-button type="primary" @click="changepasswd">确认修改</el-button>
    <br />
    <br />
    <br />
    <el-button type="danger" id="logOut" @click="logout">退出登陆</el-button>
  </div>
</template>

<script lang="ts">
function deepClone(target) {
  // 定义一个深拷贝函数  接收目标target参数
  // 定义一个变量
  let result;
  // 如果当前需要深拷贝的是一个对象的话
  if (typeof target === "object") {
    // 如果是一个数组的话
    if (Array.isArray(target)) {
      result = []; // 将result赋值为一个数组，并且执行遍历
      for (let i in target) {
        // 递归克隆数组中的每一项
        result.push(deepClone(target[i]));
      }
      // 判断如果当前的值是null的话；直接赋值为null
    } else if (target === null) {
      result = null;
      // 判断如果当前的值是一个RegExp对象的话，直接赋值
    } else if (target.constructor === RegExp) {
      result = target;
    } else {
      // 否则是普通对象，直接for in循环，递归赋值对象的所有值
      result = {};
      for (let i in target) {
        result[i] = deepClone(target[i]);
      }
    }
    // 如果不是对象的话，就是基本数据类型，那么直接赋值
  } else {
    result = target;
  }
  // 返回最终结果
  return result;
}
import axios from "axios";
import { ElMessage } from "element-plus";
export default {
  data() {
    return {
      personName: "",
      biliFollowList: [],
      weiboFollowList: [],
      BiliUpList: [],
      addBiliUpName: "",
      addBiliUpIsspecial: "0",
      WeiboUpList: [],
      addWeiboUpName: "",
      addWeiboUpIsspecial: "0",
      password: "",
      passwordtwo: "",
      newname: "",
    };
  },
  methods: {
    gotoDynasic() {
      window.open("http://127.0.0.1:8080/dynasic", "_self");
    },
    logout() {
      localStorage.removeItem("token");
      localStorage.removeItem("userName");
      // localStorage.removeItem("isLogin");
      window.open("http://127.0.0.1:8080/", "_self");
    },
    changename() {
      if (this.newname == "") {
        ElMessage.error("请输入新用户名");
      } else {
        axios
          .post("http://127.0.0.1:8000/api/chname/", {
            newname: this.newname,
          })
          .then(function (response) {
            console.log(response);
            ElMessage.success("修改成功！");
          })
          .catch(function (error) {
            console.log(error);
          });
        this.newname = "";
      }
    },
    changepasswd() {
      if (this.password != this.passwordtwo) {
        ElMessage.error("两次输入密码不同！");
      } else {
        axios
          .post("http://127.0.0.1:8000/api/chpasswd/", {
            newpassword: this.password,
          })
          .then(function (response) {
            console.log(response);
            ElMessage.success("修改成功！");
          })
          .catch(function (error) {
            console.log(error);
          });
        this.password = "";
        this.passwordtwo = "";
      }
    },
    addBiliFollow() {
      var isIn = 0;
      for (var i = 0; i < this.biliFollowList.length; i += 1) {
        if (this.biliFollowList[i].Bili_up_name == this.addBiliUpName) {
          isIn = 1;
          break;
        }
      }
      if (isIn) {
        ElMessage.error("已经关注了");
      } else {
        axios
          .post("http://127.0.0.1:8000/api/bili/followlist/", {
            Bili_is_special: this.addBiliUpIsspecial,
            Bili_follow_name: this.addBiliUpName,
          })
          .then(function (response) {
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
          });
        console.log(this.biliFollowList);
        if (this.addBiliUpIsspecial == "0") {
          this.biliFollowList.push(
            deepClone({
              Bili_up_name: this.addBiliUpName,
              Bili_is_special: "否",
            })
          );
        } else {
          this.biliFollowList.push(
            deepClone({
              Bili_up_name: this.addBiliUpName,
              Bili_is_special: "是",
            })
          );
        }
        this.addBiliUpName = "";
        this.addBiliUpIsspecial = "0";
      }
    },
    addWeiboFollow() {
      var isIn = 0;
      for (var i = 0; i < this.weiboFollowList.length; i += 1) {
        if (this.weiboFollowList[i].Weibo_up_name == this.addWeiboUpName) {
          isIn = 1;
          break;
        }
      }
      if (isIn) {
        ElMessage.error("已经关注了");
      } else {
        axios
          .post("http://127.0.0.1:8000/api/weibo/followlist/", {
            Weibo_is_special: this.addWeiboUpIsspecial,
            Weibo_follow_name: this.addWeiboUpName,
          })
          .then(function (response) {
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
          });
        console.log(this.weiboFollowList);
        if (this.addWeiboUpIsspecial == "0") {
          this.weiboFollowList.push(
            deepClone({
              Weibo_up_name: this.addWeiboUpName,
              Weibo_is_special: "否",
            })
          );
        } else {
          this.weiboFollowList.push(
            deepClone({
              Weibo_up_name: this.addWeiboUpName,
              Weibo_is_special: "是",
            })
          );
        }
        this.addWeiboUpName = "";
        this.addWeiboUpIsspecial = "0";
      }
    },
    bili_handleDelete(index) {
      console.log("delete:", index, this.biliFollowList[index].Bili_up_name);
      axios
        .delete("http://127.0.0.1:8000/api/bili/followlist/", {
          data: this.biliFollowList[index].Bili_up_name,
        })
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });
      this.biliFollowList.splice(index, 1);
      console.log("after delete:", this.biliFollowList);
    },
    weibo_handleDelete(index) {
      console.log("delete:", index, this.weiboFollowList[index].Weibo_up_name);
      axios
        .delete("http://127.0.0.1:8000/api/weibo/followlist/", {
          data: this.weiboFollowList[index].Weibo_up_name,
        })
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });
      this.weiboFollowList.splice(index, 1);
      console.log("after delete:", this.weiboFollowList);
    },
  },
  created() {
    this.personName = localStorage.userName;
    axios
      .get("http://127.0.0.1:8000/api/bili/followlist/")
      .then((response) => {
        // handle response
        var temp = response.data;
        console.log("查询ing");
        console.log(this.biliFollowList);
        this.biliFollowList = [];
        var t = { Bili_up_name: "", Bili_is_special: "" };
        for (var i = 0; i < temp.length; i++) {
          t.Bili_up_name = temp[i].Bili_up_id.Bili_up_name;
          if (temp[i].Bili_is_special == 0) t.Bili_is_special = "否";
          else t.Bili_is_special = "是";
          this.biliFollowList.push(deepClone(t));
        }
        console.log(this.biliFollowList);
      })
      .catch((error) => {
        console.log(error);
        this.errored = true;
      });
    axios
      .get("http://127.0.0.1:8000/api/weibo/followlist/")
      .then((response) => {
        // handle response
        var temp = response.data;
        console.log("查询ing");
        console.log(this.weiboFollowList);
        this.weiboFollowList = [];
        var t = { Weibo_up_name: "", Weibo_is_special: "" };
        for (var i = 0; i < temp.length; i++) {
          t.Weibo_up_name = temp[i].Weibo_up_id.Weibo_up_name;
          if (temp[i].Weibo_is_special == 0) t.Weibo_is_special = "否";
          else t.Weibo_is_special = "是";
          this.weiboFollowList.push(deepClone(t));
        }
        console.log(this.weiboFollowList);
      })
      .catch((error) => {
        console.log(error);
        this.errored = true;
      });
    this.diashow = true;
    axios
      .get("http://127.0.0.1:8000/api/bili/uplist/")
      .then((response) => {
        // handle response
        this.BiliUpList = response.data;

        console.log("查询ing");
      })
      .catch((error) => {
        console.log(error);
        this.errored = true;
      });
    axios
      .get("http://127.0.0.1:8000/api/weibo/uplist/")
      .then((response) => {
        // handle response
        this.WeiboUpList = response.data;
        console.log("查询ing");
      })
      .catch((error) => {
        console.log(error);
        this.errored = true;
      });
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/*.bg {*/
/*!*background-color: aqua;*!*/
/*background-image: url("../assets/bj.jpg");*/
/*background-size:100% 100%*/
/*}*/
#logOut {
  position: relative;
  left: 40%;
  width: 200px;
  height: 40px;
}
#back {
  position: fixed;
  right: 30px;
  top: 10px;
  z-index: 1;
  height: 40px;
  width: 120px;
}
#bigdiv {
  width: 60%;
  position: relative;
  left: 20%;
}
.login {
  position: absolute;
  top: 50%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
  -moz-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  -o-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  width: 400px;
}
.login-btn {
  background-color: whitesmoke;
}
.logo {
  font-family: "DejaVu Sans Mono";
  color: lightblue;
  font-size: 50px;
}
</style>