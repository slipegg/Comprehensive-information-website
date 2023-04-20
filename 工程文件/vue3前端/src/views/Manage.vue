<template>
  <el-button type="danger" id="logout" @click="logOut">退出登陆</el-button>
  <el-button type="warning" id="goHome" @click="gotoHome">返回主页</el-button>
  <el-container
    class="layout-container-demo"
    style="height: 730px; border: 1px solid #eee"
  >
    <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
      <el-scrollbar>
        <el-menu :default-openeds="['1', '2', '3']">
          <el-sub-menu index="1">
            <template #title>
              <el-icon><message /></el-icon>用户管理
            </template>
            <el-menu-item index="1-1" @click="common_user_manage"
              >普通用户管理</el-menu-item
            >
            <el-menu-item index="1-2" @click="super_user_manage"
              >超级用户管理</el-menu-item
            >
          </el-sub-menu>
          <el-sub-menu index="2">
            <template #title>
              <el-icon><icon-menu /></el-icon>动态管理
            </template>
            <el-menu-item index="2-1" @click="bili_dy_manage"
              >b站动态管理</el-menu-item
            >
            <el-menu-item index="2-2" @click="weibo_dy_manage"
              >微博动态管理</el-menu-item
            >
          </el-sub-menu>
          <el-sub-menu index="3">
            <template #title>
              <el-icon><icon-menu /></el-icon>热榜管理
            </template>
            <el-menu-item index="2-1" @click="all_hot_manage"
              >热榜管理</el-menu-item
            >
          </el-sub-menu>
        </el-menu>
      </el-scrollbar>
    </el-aside>

    <el-container v-if="common_user_manage_show">
      <el-header style="font-size: 12px">
        <el-button size="20" type="primary" @click="handleAdd()" class="addUser"
          >添加用户</el-button
        >
      </el-header>

      <el-main>
        <el-scrollbar>
          <el-table :data="normalUserData" style="width: 100%">
            <el-table-column label="注册时间" prop="date_joined" />
            <el-table-column label="昵称" prop="username" />
            <!-- <el-table-column label="邮箱" prop="email" />
            <el-table-column label="性别" prop="gender" /> -->
            <el-table-column align="right">
              <template #header>
                <el-input
                  v-model="search"
                  size="small"
                  placeholder="Type to search"
                />
              </template>
              <template #default="scope">
                <el-button size="small" @click="handleEdit(scope.$index)"
                  >Edit</el-button
                >
                <el-button
                  size="small"
                  type="danger"
                  @click="handleDelete(scope.$index)"
                  >Delete</el-button
                >
              </template>
            </el-table-column>
          </el-table>
        </el-scrollbar>
      </el-main>
    </el-container>
    <el-container v-if="super_user_manage_show">
      <el-header style="font-size: 12px">
        <el-button
          size="20"
          type="primary"
          @click="handleAddSuper()"
          class="addUser"
          >添加超级用户</el-button
        >
      </el-header>
      <el-main>
        <el-scrollbar>
          <el-table :data="superUserData" style="width: 100%">
            <el-table-column label="注册时间" prop="date_joined" />
            <el-table-column label="昵称" prop="username" />
            <!-- <el-table-column label="邮箱" prop="email" />
            <el-table-column label="性别" prop="gender" /> -->
            <el-table-column align="right">
              <template #header>
                <el-input
                  v-model="search"
                  size="small"
                  placeholder="Type to search"
                />
              </template>
              <template #default="scope">
                <el-button size="small" @click="handleSuperEdit(scope.$index)"
                  >Edit</el-button
                >
                <el-button
                  size="small"
                  type="danger"
                  @click="handleDeleteSuperUser(scope.$index)"
                  >Delete</el-button
                >
              </template>
            </el-table-column>
          </el-table>
        </el-scrollbar>
      </el-main>
    </el-container>
    <el-container v-if="bili_dy_show">
      <el-header style="font-size: 12px">
        <el-button
          size="20"
          type="primary"
          @click="handleAddBiliUp()"
          class="addUser"
          >添加b站用户</el-button
        >
      </el-header>
      <el-main>
        <el-scrollbar>
          <el-table :data="bili_up_data" style="width: 100%">
            <el-table-column label="昵称" prop="Bili_up_name" />
            <el-table-column label="UID" prop="Bili_up_id" />
            <el-table-column label="头像" prop="Bili_up_face_url" />
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
                  @click="bili_up_handle_del(scope.$index)"
                  >删除</el-button
                >
              </template>
            </el-table-column>
          </el-table>
        </el-scrollbar>
      </el-main>
    </el-container>
    <el-container v-if="weibo_dy_show">
      <el-header style="font-size: 12px">
        <el-button
          size="20"
          type="primary"
          @click="handleAddWeiboUp()"
          class="addUser"
          >添加微博用户</el-button
        >
      </el-header>
      <el-main>
        <el-scrollbar>
          <el-table :data="weibo_up_data" style="width: 100%">
            <el-table-column label="昵称" prop="Weibo_up_name" />
            <el-table-column label="UID" prop="Weibo_up_id" />
            <el-table-column label="头像" prop="Weibo_up_face_url" />
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
                  @click="weibo_up_handle_del(scope.$index)"
                  >删除</el-button
                >
              </template>
            </el-table-column>
          </el-table>
        </el-scrollbar>
      </el-main>
    </el-container>
    <el-container v-if="allhotShow">
      <el-header style="font-size: 12px"> </el-header>
      <el-main>
        <el-row>
          微博热榜刷新时间：
          <div>
            <el-input
              v-model="weiboHotTime"
              class="w-50 m-2"
              size="small"
              placeholder="Please Input"
            />
          </div>
          <span>分钟</span>
        </el-row>

        <el-row
          >知乎热榜刷新时间：
          <div>
            <el-input
              v-model="zhihuHotTime"
              class="w-50 m-2"
              size="small"
              placeholder="Please Input"
            />
          </div>
          <span>分钟</span>
        </el-row>
        <el-row>
          b站热榜刷新时间：
          <div>
            <el-input
              v-model="biliHotTime"
              class="w-50 m-2"
              size="small"
              placeholder="Please Input"
            />
          </div>
          <span>分钟</span>
        </el-row>
        <hr />
        <el-row>
          微博动态刷新时间：
          <div>
            <el-input
              v-model="weiboDynasicTime"
              class="w-50 m-2"
              size="small"
              placeholder="Please Input"
            />
          </div>
          <span>分钟</span>
        </el-row>
        <el-row>
          b站动态刷新时间：
          <div>
            <el-input
              v-model="biliDynasicTime"
              class="w-50 m-2"
              size="small"
              placeholder="Please Input"
            />
          </div>
          <span>分钟</span>
        </el-row>
        <hr />
        <el-button id="changetimeButton" type="primary" @click="change_time()"
          >确定</el-button
        >
      </el-main>
    </el-container>
  </el-container>
  <!-- 微博动态管理弹出框 -->
  <el-dialog
    v-model="weiboUpDiaShow"
    draggable="true"
    close-on-press-escape="false"
    title="增加微博动态用户"
  >
    <el-row>
      <span>昵称：</span>
      <div>
        <el-input
          v-model="newWeiboUp.Weibo_up_name"
          class="w-50 m-2"
          size="small"
          placeholder="Please Input"
        />
      </div>
      <span>UID：</span>
      <div class="dia_name">
        <el-input
          v-model="newWeiboUp.Weibo_up_id"
          class="w-50 m-2"
          size="small"
          placeholder="Please Input"
        />
      </div>
      <span>头像：</span>
      <div class="dia_name">
        <el-input
          v-model="newWeiboUp.Weibo_up_face_url"
          class="w-50 m-2"
          size="small"
          placeholder="Please Input"
        />
      </div>
    </el-row>
    <span class="dialog-footer">
      <el-button @click="weiboUpDiaShow = false">Cancel</el-button>
      <el-button type="primary" @click="close_weibo_up_dia">Confirm</el-button>
    </span>
  </el-dialog>
  <!-- b站动态管理弹出框 -->
  <el-dialog
    v-model="biliUpDiaShow"
    draggable="true"
    close-on-press-escape="false"
    title="增加b站动态用户"
  >
    <el-row>
      <span>昵称：</span>
      <div>
        <el-input
          v-model="newBiliUp.Bili_up_name"
          class="w-50 m-2"
          size="small"
          placeholder="Please Input"
        />
      </div>
      <span>UID：</span>
      <div class="dia_name">
        <el-input
          v-model="newBiliUp.Bili_up_id"
          class="w-50 m-2"
          size="small"
          placeholder="Please Input"
        />
      </div>
      <span>头像链接：</span>
      <div class="dia_face_url">
        <el-input
          v-model="newBiliUp.Bili_up_face_url"
          class="w-100 m-2"
          size="small"
          placeholder="Please Input"
        />
      </div>
    </el-row>
    <span class="dialog-footer">
      <el-button @click="biliUpDiaShow = false">Cancel</el-button>
      <el-button type="primary" @click="close_bili_up_dia">Confirm</el-button>
    </span>
  </el-dialog>
  <!-- 超级用户弹出框 -->
  <el-dialog
    v-model="superdiashow"
    draggable="true"
    close-on-press-escape="false"
    title="添加超级用户"
  >
    <el-row>
      <span>昵称：</span>
      <div class="dia_name">
        <el-input
          v-model="newSuperUser.name"
          class="w-50 m-2"
          size="small"
          placeholder="Please Input"
        />
      </div>
    </el-row>
    <el-row>
      <span>密码：</span>
      <div>
        <el-input
          v-model="newSuperUser.passwd"
          class="w-50 m-2"
          size="small"
          placeholder="Please Input"
        />
      </div>
    </el-row>

    <span class="dialog-footer">
      <el-button @click="superdiashow = false">Cancel</el-button>
      <el-button type="primary" @click="close_super_dia">Confirme</el-button>
    </span>
  </el-dialog>
  <!-- 普通用户弹窗 -->
  <el-dialog
    v-model="diashow"
    draggable="true"
    close-on-press-escape="false"
    width="70%"
    top="3vh"
  >
    <h1 v-text="get_tip()" class="dia_tip"></h1>
    <el-row v-if="diatype != 'Edit'">
      <span>昵称：</span>
      <div class="dia_name">
        <el-input
          v-model="tempData.username"
          class="w-50 m-2"
          size="small"
          placeholder="Please Input"
        />
      </div>
    </el-row>
    <br />
    <el-row>
      <span>密码：</span>
      <div>
        <el-input
          v-model="tempData.passwd"
          class="w-50 m-2"
          size="small"
          placeholder="Please Input"
        />
      </div>
    </el-row>
    <br />
    <!--<p>b站关注的人</p>

    <el-table :data="tempData.bili_follow" style="width: 100%" max-height="200">
      <el-table-column label="姓名" prop="name"></el-table-column>
      <el-table-column label="是否特别关注" prop="is_special">
        <template #default="scope">
          <el-select v-model="tempData.bili_follow[scope.$index].is_special">
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
    <span>姓名：</span>
    <el-input
      v-model="bili_new_follow.name"
      placeholder="Please Input"
      style="width: 200px"
    />
    <span>是否特别关注：</span>
    <el-select v-model="bili_new_follow.is_special">
      <el-option label="是" value="true" />
      <el-option label="否" value="false" />
    </el-select>
    <el-button size="small" type="primary" @click="bili_handleAdd()"
      >添加</el-button
    >
    <p>微博关注的人</p>

    <el-table
      :data="tempData.weibo_follow"
      style="width: 100%"
      max-height="200"
    >
      <el-table-column label="姓名" prop="name"></el-table-column>
      <el-table-column label="是否特别关注" prop="is_special">
        <template #default="scope">
          <el-select v-model="tempData.weibo_follow[scope.$index].is_special">
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
    <span>姓名：</span>
    <el-input
      v-model="weibo_new_follow.name"
      placeholder="Please Input"
      style="width: 200px"
    />
    <span>是否特别关注：</span>
    <el-select v-model="weibo_new_follow.is_special">
      <el-option label="是" value="true" />
      <el-option label="否" value="false" />
    </el-select>
    <el-button size="small" type="primary" @click="weibo_handleAdd()"
      >添加</el-button
    >
    <br /> -->
    <span class="dialog-footer">
      <el-button @click="diashow = false">Cancel</el-button>
      <el-button type="primary" @click="close_dia">Confirm</el-button>
    </span>
  </el-dialog>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import { Menu as IconMenu, Message, Setting } from "@element-plus/icons-vue";
import { reactive, computed } from "vue";
const input1 = ref("233");
// const tableData = [
//   {
//     date: "2016-05-04",
//     name: "Tom",
//     email: "233@163.com",
//     gender: "男",
//   },
//   {
//     date: "2016-05-02",
//     name: "John",
//     email: "4532@qq.com",
//     gender: "女",
//   },
// ];
const form = reactive({
  name: "",
  region: "",
  date1: "",
  date2: "",
  delivery: false,
  type: [],
  resource: "",
  desc: "",
});
const search = ref("");
// const dialogTableVisible = ref(false);
// const filterTableData = computed(() =>
//   tableData.filter(
//     (data) =>
//       !search.value ||
//       data.name.toLowerCase().includes(search.value.toLowerCase())
//   )
// );
</script>

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
import { ElMessage } from "element-plus";
import axios from "axios";
import moment from "moment";
axios.defaults.withCredentials = true;
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
export default {
  data() {
    return {
      superUserData: [],
      normalUserData: [],
      biliHotTime: 20,
      weiboHotTime: 20,
      zhihuHotTime: 20,
      biliDynasicTime: 20,
      weiboDynasicTime: 20,
      newWeiboUp: {
        Weibo_up_name: "",
        Weibo_up_id: "",
        Weibo_up_face_url: "",
      },
      newBiliUp: {
        Bili_up_name: "",
        Bili_up_id: "",
        Bili_up_face_url: "",
      },
      newSuperUser: {
        name: "",
        passwd: "",
      },
      superdiashow: false,
      common_user_manage_show: true,
      super_user_manage_show: false,
      bili_dy_show: false,
      weibo_dy_show: false,
      biliUpDiaShow: false,
      weiboUpDiaShow: false,
      allhotShow: false,
      weibo_up_data: [],
      // [
      //   {
      //     name: "__warma__",
      //     uid: 34543431,
      //   },
      //   {
      //     name: "2233",
      //     uid: 82393,
      //   },
      // ],
      bili_up_data: [],
      // [
      //   {
      //     name: "warma",
      //     uid: 34543431,
      //   },
      //   {
      //     name: "多罗西123",
      //     uid: 82393,
      //   },
      // ],
      super_user_data: [
        {
          date: "2016-05-04",
          name: "Root",
          email: "233@163.com",
          gender: "男",
        },
        {
          date: "2017-05-04",
          name: "Root2",
          email: "566@163.com",
          gender: "男",
        },
      ],
      chosed_index: -1,
      diashow: false,
      diatype: "",
      bili_new_follow: {
        name: "",
        is_special: "false",
      },
      weibo_new_follow: {
        name: "",
        is_special: "false",
      },
      tempData: {
        date: "",
        passwd: "",
        name: "",
        email: "",
        gender: "",
        bili_follow: [],
        weibo_follow: [],
      },
    };
  },
  methods: {
    change_time() {
      axios
        .post("http://127.0.0.1:8000/api/timeManage", {
          biliDynasicTime: this.biliDynasicTime,
          biliHotTime: this.biliHotTime,
          weiboDynasicTime: this.weiboDynasicTime,
          weiboHotTime: this.weiboHotTime,
          zhihuHotTime: this.zhihuHotTime,
        })
        .then((res) => {
          console.log(res);
          if (res.data.status == true) {
            ElMessage({
              message: "修改成功！",
              type: "success",
            });
          } else {
            ElMessage({
              message: res.data.data,
              type: "error",
            });
          }
        });
    },
    logOut() {
      localStorage.removeItem("token");
      localStorage.removeItem("userName");
      localStorage.removeItem("isLogin");
      window.open("http://127.0.0.1:8080/", "_self");
    },
    gotoHome() {
      window.open("http://127.0.0.1:8080", "_self");
    },
    handleAddSuper() {
      this.superdiashow = true;
    },
    common_user_manage() {
      this.super_user_manage_show = false;
      this.common_user_manage_show = true;
      this.bili_dy_show = false;
      this.weibo_dy_show = false;
      this.allhotShow = false;
    },
    super_user_manage() {
      this.super_user_manage_show = true;
      this.common_user_manage_show = false;
      this.bili_dy_show = false;
      this.weibo_dy_show = false;
      this.allhotShow = false;
    },
    handleAdd() {
      this.tempData.username = "";
      this.tempData.passwd = "";
      this.diatype = "Add";
      this.diashow = true;
    },
    handleEdit(index) {
      this.diatype = "Edit";
      this.diashow = true;
      this.tempData = deepClone(this.normalUserData[index]);
      this.chosed_index = index;
    },
    handleSuperEdit(index) {
      this.diatype = "Edit";
      this.diashow = true;
      this.tempData = deepClone(this.superUserData[index]);
      console.log("tempData", this.tempData);
      this.chosed_index = index;
    },
    handleDelete(index) {
      axios
        .post("http://127.0.0.1:8000/api/normalUser", {
          data: this.normalUserData[index],
        })
        .then((res) => {
          console.log(res);
          if (res.data.status == true) {
            ElMessage({
              message: "删除成功！",
              type: "success",
            });
            this.normalUserData.splice(index, 1);
          } else {
            ElMessage({
              message: "删除失败！",
              type: "error",
            });
          }
        });
    },
    get_tip() {
      if (this.diatype == "Add") {
        return "添加用户";
      } else if (this.diatype == "Edit") {
        return "修改用户信息";
      }
    },
    show_chose(gender) {
      console.log(gender);
      this.$forceUpdate();
    },
    close_dia() {
      console.log("close_dia", this.tempData.username, this.tempData.passwd);
      if (this.diatype == "Edit") {
        console.log("Edit", this.tempData.username, this.tempData.passwd);
        if (!this.tempData.passwd) {
          ElMessage.error("密码不能为空");
        } else {
          this.diashow = false;
          axios
            .post("http://127.0.0.1:8000/api/rootChangePasswd/", {
              id: this.tempData.id,
              username: this.tempData.username,
              newpassword: this.tempData.passwd,
            })
            .then((res) => {
              ElMessage({
                message: "修改成功！",
                type: "success",
              });
            })
            .catch(function (error) {
              console.log(error);
            });
        }
      } else if (this.diatype == "Add") {
        console.log("this.tempData.name:", this.tempData.username);
        this.diashow = false;
        axios
          .post("http://127.0.0.1:8000/api/register/", {
            username: this.tempData.username,
            password: this.tempData.passwd,
          })
          .then((res) => {
            if (res.data.status) {
              ElMessage({
                message: "添加成功！",
                type: "success",
              });
              var time1 = moment().format("YYYY-MM-DD HH:mm:ss");
              this.normalUserData.push({
                date_joined: time1,
                username: deepClone(this.tempData.username),
              });
            } else {
              this.$message.error(res.data.data);
            }
          })
          .catch(function (error) {
            console.log(error);
          });
      }
      // for (let i in this.tempData) {
      //   this.tempData[i] = "";
      // }
    },
    bili_handleDelete(index) {
      this.tempData["bili_follow"].splice(index, 1);
    },
    bili_handleAdd() {
      if (this.bili_new_follow.name == "") {
        ElMessage({
          message: "请输入姓名！",
          type: "warning",
        });
      } else {
        this.tempData["bili_follow"].push(deepClone(this.bili_new_follow));
        this.bili_new_follow.name = "";
        this.bili_new_follow.is_special = "false";
        ElMessage({
          message: "添加已暂存，请及时保存！",
          type: "success",
        });
      }
    },
    weibo_handleDelete(index) {
      this.tempData["weibo_follow"].splice(index, 1);
    },
    weibo_handleAdd() {
      if (this.weibo_new_follow.name == "") {
        ElMessage({
          message: "请输入姓名！",
          type: "warning",
        });
      } else {
        this.tempData["weibo_follow"].push(deepClone(this.weibo_new_follow));
        this.weibo_new_follow.name = "";
        this.weibo_new_follow.is_special = "false";
        ElMessage({
          message: "添加已暂存，请及时保存！",
          type: "success",
        });
      }
    },
    handleDeleteSuperUser(index) {
      axios
        .post("http://127.0.0.1:8000/api/superUser", {
          data: this.superUserData[index],
        })
        .then((res) => {
          console.log(res);
          if (res.data.status == true) {
            ElMessage({
              message: "删除成功！",
              type: "success",
            });
            this.superUserData.splice(index, 1);
          } else {
            ElMessage({
              message: "删除失败！",
              type: "error",
            });
          }
        });
    },
    close_super_dia() {
      this.superdiashow = false;
      axios
        .post("http://127.0.0.1:8000/api/register/", {
          username: this.newSuperUser.name,
          password: this.newSuperUser.password,
          is_staff: "True",
        })
        .then((res) => {
          if (res.data.status) {
            ElMessage({
              message: "添加成功！",
              type: "success",
            });
            var time1 = moment().format("YYYY-MM-DD HH:mm:ss");
            this.superUserData.push({
              date_joined: time1,
              username: this.newSuperUser.name,
            });
          } else {
            this.$message.error(res.data.data);
          }
        });
      for (let i in this.newSuperUser) {
        this.newSuperUser[i] = "";
      }
    },
    bili_dy_manage() {
      this.super_user_manage_show = false;
      this.common_user_manage_show = false;
      this.bili_dy_show = true;
      this.weibo_dy_show = false;
      this.allhotShow = false;
    },
    weibo_dy_manage() {
      this.super_user_manage_show = false;
      this.common_user_manage_show = false;
      this.bili_dy_show = false;
      this.weibo_dy_show = true;
      this.allhotShow = false;
    },
    bili_up_handle_del(index) {
      axios
        .delete("http://127.0.0.1:8000/api/bili/uplist/", {
          data: this.bili_up_data[index],
        })
        .then((res) => {
          console.log(res);
          if (res.data.status == true) {
            ElMessage({
              message: "删除成功！",
              type: "success",
            });
            console.log(res);
            this.bili_up_data.splice(index, 1);
          } else {
            ElMessage({
              message: "删除失败！",
              type: "error",
            });
          }
        });
    },
    handleAddBiliUp() {
      this.biliUpDiaShow = true;
    },
    close_bili_up_dia() {
      console.log(this.newBiliUp);
      axios
        .post("http://127.0.0.1:8000/api/bili/uplist/", this.newBiliUp)
        .then((res) => {
          console.log(res);
          if (res.data.status == true) {
            ElMessage({
              message: "添加成功！",
              type: "success",
            });
            console.log(res);
            this.bili_up_data.push(this.newBiliUp);
            this.biliUpDiaShow = false;
          } else {
            ElMessage({
              message: "添加失败！" + res.data.data,
              type: "error",
            });
          }
        });
    },
    weibo_up_handle_del(index) {
      axios
        .delete("http://127.0.0.1:8000/api/weibo/uplist/", {
          data: this.weibo_up_data[index],
        })
        .then((res) => {
          console.log(res);
          if (res.data.status == true) {
            ElMessage({
              message: "删除成功！",
              type: "success",
            });
            console.log(res);
            this.weibo_up_data.splice(index, 1);
          } else {
            ElMessage({
              message: "删除失败！",
              type: "error",
            });
          }
        });
    },
    handleAddWeiboUp() {
      this.weiboUpDiaShow = true;
    },
    close_weibo_up_dia() {
      console.log(this.newWeiboUp);
      axios
        .post("http://127.0.0.1:8000/api/weibo/uplist/", this.newWeiboUp)
        .then((res) => {
          console.log(res);
          if (res.data.status == true) {
            ElMessage({
              message: "添加成功！",
              type: "success",
            });
            console.log(res);
            this.weibo_up_data.push(this.newWeiboUp);
            this.weiboUpDiaShow = false;
          } else {
            ElMessage({
              message: "添加失败！" + res.data.data,
              type: "error",
            });
          }
        });
    },
    all_hot_manage() {
      this.super_user_manage_show = false;
      this.common_user_manage_show = false;
      this.bili_dy_show = false;
      this.weibo_dy_show = false;
      this.allhotShow = true;
    },
    change_hot_time() {
      ElMessage({
        message: "修改成功！",
        type: "success",
      });
    },
  },
  async created() {
    // if (localStorage.userName != "root") {
    //   window.open("http://127.0.0.1:8080/", "_self");
    // }
    axios.get("http://127.0.0.1:8000/api/isRoot").then((response) => {
      // console.log("response", response);
      if (!response.data.status) {
        window.open("http://127.0.0.1:8080/", "_self");
      }
    });
    axios.get("http://127.0.0.1:8000/api/timeManage").then((response) => {
      console.log("timeManage", response);
      this.biliHotTime = response.data.biliHotTime;
      this.weiboHotTime = response.data.weiboHotTime;
      this.zhihuHotTime = response.data.zhihuHotTime;
      this.weiboDynasicTime = response.data.weiboDynasicTime;
      this.biliDynasicTime = response.data.biliDynasicTime;
    });
    axios
      .get("http://127.0.0.1:8000/api/normalUser")
      .then((response) => {
        // handle response
        this.normalUserData = response.data;
        console.log("normalUserData:", this.normalUserData);

        var moment = require("moment-timezone");
        var tz = "Asia/Choibalsan"; //时区
        for (var i = 0; i < this.normalUserData.length; i++) {
          this.normalUserData[i]["date_joined"] = moment
            .utc(this.normalUserData[i]["date_joined"])
            .tz(tz)
            .format("YYYY-MM-DD HH:mm:ss");
        }
      })
      .catch((error) => {
        console.log(error);
      });
    axios
      .get("http://127.0.0.1:8000/api/superUser")
      .then((response) => {
        // handle response
        this.superUserData = response.data;
        var moment = require("moment-timezone");
        var tz = "Asia/Choibalsan"; //时区
        for (var i = 0; i < this.superUserData.length; i++) {
          this.superUserData[i]["date_joined"] = moment
            .utc(this.superUserData[i]["date_joined"])
            .tz(tz)
            .format("YYYY-MM-DD HH:mm:ss");
        }
      })
      .catch((error) => {
        console.log(error);
      });
    axios
      .get("http://127.0.0.1:8000/api/bili/uplist")
      .then((response) => {
        // handle response
        this.bili_up_data = response.data;
        console.log("查询ing");
      })
      .catch((error) => {
        console.log(error);
      });
    axios
      .get("http://127.0.0.1:8000/api/weibo/uplist")
      .then((response) => {
        // handle response
        this.weibo_up_data = response.data;
        console.log("查询ing");
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>

<style scoped>
#changetimeButton {
  position: relative;
  left: 20px;
  width: 80px;
  height: 30px;
}
#goHome {
  position: fixed;
  left: 20px;
  bottom: 16%;
  width: 150px;
  height: 40px;
  z-index: 10;
}
#logout {
  position: fixed;
  left: 33px;
  top: 90%;
  width: 150px;
  height: 40px;
  z-index: 10;
}
.dia_tip {
  position: absolute;
  top: -5px;
}
.addUser {
  position: relative;
  left: -10px;
  top: 14px;
}
.layout-container-demo .el-header {
  position: relative;
  background-color: #b3c0d1;
  color: var(--el-text-color-primary);
}
.layout-container-demo .el-aside {
  width: 240px;
  color: var(--el-text-color-primary);
  background: #fff !important;
  border-right: solid 1px #e6e6e6;
  box-sizing: border-box;
}
.layout-container-demo .el-menu {
  border-right: none;
}
.layout-container-demo .el-main {
  padding: 0;
}
.layout-container-demo .toolbar {
  position: absolute;
  display: inline-flex;
  align-items: center;
  top: 50%;
  right: 20px;
  transform: translateY(-50%);
}
</style>
