<template>
  <el-button type="primary" id="mangeFollow" @click="gotoPerson"
    >个人中心</el-button
  >
  <el-button type="primary" id="hotListShow" @click="gotoHot">热榜</el-button>
  <el-button type="danger" id="manageShow" @click="gotoManage" v-if="isRoot"
    >管理中心</el-button
  >
  <meta name="referrer" content="no-referrer" />
  <el-carousel
    trigger="click"
    height="790px"
    indicator-position="outside"
    :autoplay="false"
  >
    <el-carousel-item v-for="item in 2" :key="item">
      <div
        v-if="item == 1"
        class="infinite-list-wrapper"
        style="overflow: auto"
      >
        <h1 style="text-align: center">微博动态</h1>
        <ul v-infinite-scroll="load" :infinite-scroll-immediate="false">
          <el-space
            direction="vertical"
            v-for="(n, i) in weibodynasic.length"
            :key="i"
          >
            <div class="dyna_body" v-if="true">
              <div class="dy_card_head">
                <div class="up_face">
                  <el-avatar
                    :size="50"
                    :src="weibodynasic[i].Weibo_up_id.Weibo_up_face_url"
                  />
                </div>
                <div class="up_name">
                  {{ weibodynasic[i].Weibo_up_id.Weibo_up_name }}
                </div>
                <div class="dy_time">
                  {{ changeTime(weibodynasic[i].Weibo_post_time) }}
                </div>
              </div>

              <div class="dy_content">
                <p
                  v-html="weibodynasic[i].Weibo_content"
                  @click="goto_weibo(weibodynasic[i].Weibo_url_id)"
                ></p>
                <div
                  class="bili_img_div"
                  v-if="
                    changePicList(weibodynasic[i].Weibo_pic_urls).length > 0
                  "
                >
                  <el-image
                    v-for="(j, key) in changePicList(
                      weibodynasic[i].Weibo_pic_urls
                    ).length"
                    :key="key"
                    style="width: 103px; height: 104px"
                    :src="changePicList(weibodynasic[i].Weibo_pic_urls)[j - 1]"
                    :fit="cover"
                    :preview-src-list="
                      changePicList(weibodynasic[i].Weibo_pic_urls)
                    "
                    :initial-index="j - 1"
                  />
                </div>
              </div>
              <div
                class="dy_tail"
                @click="goto_weibo(weibodynasic[i].Weibo_url_id)"
              >
                <img class="share_img" src="../static/share.png" />
                {{ weibodynasic[i].Weibo_share }}
                <img class="comment_img" src="../static/comment.png" />
                {{ weibodynasic[i].Weibo_comment }}
                <img class="like_img" src="../static/like.png" />
                {{ weibodynasic[i].Weibo_like }}--{{ i }}
              </div>
            </div>
          </el-space>
        </ul>
        <p v-if="loading">Loading...</p>
        <p v-if="noMore">No more</p>
      </div>
      <div
        v-if="item == 2"
        class="infinite-list-wrapper"
        style="overflow: auto"
      >
        <h1 style="text-align: center">b站动态</h1>
        <ul v-infinite-scroll="load" :infinite-scroll-immediate="false">
          <el-space
            direction="vertical"
            v-for="(n, i) in bilidynasic.length"
            :key="i"
          >
            <div class="dyna_body" v-if="true">
              <div class="dy_card_head">
                <div class="up_face">
                  <el-avatar
                    :size="50"
                    :src="bilidynasic[i].Bili_up_id.Bili_up_face_url"
                  />
                </div>
                <div class="up_name">
                  {{ bilidynasic[i].Bili_up_id.Bili_up_name }}
                </div>
                <div class="dy_time">
                  {{ changeTime(bilidynasic[i].Bili_post_time) }}
                </div>
              </div>

              <div class="dy_content">
                <p @click="goto_bili_dy(bilidynasic[i].Bili_url_id)">
                  {{ bilidynasic[i].Bili_content }}
                </p>
                <p></p>
                <div
                  class="bili_img_div"
                  v-if="changePicList(bilidynasic[i].Bili_pic_urls).length > 0"
                >
                  <el-image
                    v-for="(j, key) in changePicList(
                      bilidynasic[i].Bili_pic_urls
                    ).length"
                    :key="key"
                    style="width: 103px; height: 104px"
                    :src="changePicList(bilidynasic[i].Bili_pic_urls)[j - 1]"
                    :fit="cover"
                    :preview-src-list="
                      changePicList(bilidynasic[i].Bili_pic_urls)
                    "
                    :initial-index="j - 1"
                  />
                </div>
                <div
                  class="bili_video"
                  @click="goto_bili_video(bilidynasic[i].Bili_video_url)"
                  v-if="bilidynasic[i].Bili_type == 2"
                >
                  <div class="video_pic">
                    <el-image
                      :src="bilidynasic[i].Bili_video_pic_url"
                      :fit="contain"
                    />
                  </div>
                  <div
                    class="video_title"
                    v-text="get_title(bilidynasic[i].Bili_video_title)"
                  ></div>
                  <div
                    class="video_desc"
                    v-text="get_desc(bilidynasic[i].Bili_video_desc)"
                  ></div>
                </div>
              </div>
              <div class="dy_tail">
                <img class="share_img" src="../static/share.png" />
                {{ bilidynasic[i].Bili_share }}
                <img class="comment_img" src="../static/comment.png" />
                {{ bilidynasic[i].Bili_comment }}
                <img class="like_img" src="../static/like.png" />
                {{ bilidynasic[i].Bili_like }}--{{ i }}
              </div>
            </div>
          </el-space>
        </ul>
        <p v-if="loading">Loading...</p>
        <p v-if="noMore">No more</p>
      </div>
    </el-carousel-item>
  </el-carousel>
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
import { useRouter } from "vue-router";
export default {
  data() {
    return {
      isRoot: false,
      temp: "",
      biliFollowList: [],
      weiboFollowList: [],
      diashow: false,
      bilidynasic: {},
      weibodynasic: {},
      BiliUpList: [],
      addBiliUpName: "",
      addBiliUpIsspecial: "0",
      WeiboUpList: [],
      addWeiboUpName: "",
      addWeiboUpIsspecial: "0",
    };
  },

  methods: {
    gotoManage() {
      window.open("http://127.0.0.1:8080/manage", "_self");
    },
    gotoHot() {
      // this.$router.push({ path: "/" });
      window.open("http://127.0.0.1:8080/", "_self");
    },
    gotoPerson() {
      // this.$router.push({ path: "/person" });
      window.open("http://127.0.0.1:8080/person", "_self");
    },
    get_title(title) {
      if (title.length > 40) return title.substring(0, 40) + "...";
      else return title;
    },
    get_desc(desc) {
      if (desc.length > 60) return desc.substring(0, 60) + "...";
      else return desc;
    },
    goto_bili_video(video_url) {
      window.open(video_url);
    },
    goto_bili_dy(dy_id) {
      window.open("https://t.bilibili.com/" + dy_id);
      // console.log("https://t.bilibili.com/" + dy_id);
      // alert("https://t.bilibili.com/" + dy_id);
    },
    goto_weibo(weibo_id) {
      window.open("https://m.weibo.cn/detail/" + weibo_id);
    },
    changePicList(str) {
      var tpic = JSON.parse(str); //(this.bilidynasic[index].Bili_pic_urls);
      if (tpic == null) {
        return [];
      }
      return tpic;
    },
    changeBiliPicList(index) {
      console.log("转换ing");
      var tpic = JSON.parse(this.bilidynasic[index].Bili_pic_urls);
      if (tpic == null) {
        return [];
      }
      console.log(tpic);
      return tpic;
    },
    changeTime(stamp) {
      var date = new Date(stamp * 1000);
      var Y = date.getFullYear() + "-";
      var M =
        (date.getMonth() + 1 < 10
          ? "0" + (date.getMonth() + 1)
          : date.getMonth() + 1) + "-";
      var D =
        (date.getDate() < 10 ? "0" + date.getDate() : date.getDate()) + " ";

      var h =
        (date.getHours() < 10 ? "0" + date.getHours() : date.getHours()) + ":";

      var m =
        (date.getMinutes() < 10 ? "0" + date.getMinutes() : date.getMinutes()) +
        ":";

      var s =
        date.getSeconds() < 10 ? "0" + date.getSeconds() : date.getSeconds();
      return Y + M + D + h + m + s;
    },
  },
  comments: {},

  created() {
    axios.get("http://127.0.0.1:8000/api/isRoot").then((response) => {
      this.isRoot = response.data.status;
    });
    axios
      .get("http://127.0.0.1:8000/api/bili/dynasic/")
      .then((response) => {
        // handle response
        this.bilidynasic = response.data;
        console.log("查询ing");
      })
      .catch((error) => {
        console.log(error);
      });
    axios
      .get("http://127.0.0.1:8000/api/weibo/dynasic/")
      .then((response) => {
        // handle response
        this.weibodynasic = response.data;
        console.log("查询ing");
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>

<style>
#manageShow {
  position: fixed;
  left: 30px;
  bottom: 10px;
  z-index: 1;
  height: 40px;
  width: 120px;
}
#mangeFollow {
  position: fixed;
  right: 30px;
  top: 10px;
  z-index: 1;
  height: 40px;
  width: 120px;
}
#hotListShow {
  position: fixed;
  left: 30px;
  top: 10px;
  z-index: 1;
  height: 40px;
  width: 120px;
}
.bili_img_div {
  position: relative;
  width: 320px;
  /* border: 1px solid black; */
  z-index: 3;
}
.video_title {
  position: absolute;
  left: 210px;
  top: 2px;
  height: 40px;
  font-size: 14px;
  line-height: 19px;
  /* width: 200px; */
  color: #212121;
  /* border: 1px solid black; */
}
.video_desc {
  position: absolute;
  left: 210px;
  top: 45px;
  /* border: 1px solid black; */
  font-size: 12px;
  line-height: 19px;
  height: 58px;
  /* width: 500px; */
  margin-top: 8px;
  color: #666;
}
.video_pic {
  position: relative;
  width: 200px;
  height: 100px;
}
.bili_video {
  position: relative;
  width: 800px;
  height: 125px;
  border: 1px solid black;
}

.test {
  width: 400px;
  height: 500px;
}
.share_img {
  width: 50px;
  /* border: 1px solid black; */
}
.share {
  position: absolute;
}
.dy_tail {
  position: relative;
  width: 80%;
  left: 63px;
  /* height: 30px; */
  bottom: -5px;
  margin: 5px;
  /* border: 1px solid black; */
  font-size: 12px;
  color: #99a2aa;
}
.share_img {
  width: 20px;
  /* border: 1px solid black; */
}
.comment_img {
  width: 20px;
  /* border: 1px solid black; */
}
.like_img {
  width: 20px;
  /* border: 1px solid black; */
}
.dy_card_head {
  position: relative;
  width: 900px;
  height: 60px;
  background-color: rgb(191, 206, 228);
  /* border: 1px solid black; */
}
.dy_content {
  white-space: pre-wrap; /* \n文本换行 */
  position: relative;
  width: 90%;
  left: 63px;
  top: 5px;
  /* border: 1px solid black; */
  font-size: 14px;
  line-height: 22px;
  color: inherit;
  letter-spacing: 0.5px;
}
.dy_time {
  position: absolute;
  left: 60px;
  top: 30px;
  font-size: 13px;
  color: #999;
  /* border: 1px solid black; */
}

.dyna_body {
  width: 900px;
  /* height: 100%; */
  display: table;
  clear: both;

  overflow: auto;
  border: 1px solid black;
  position: relative;
  /* left: 500px; */
  /* background-color: rgb(255, 255, 255); */
  background-color: rgb(219, 219, 241);
}
.up_face {
  position: absolute;
  /* width: 100px; */
  /* border: 1px solid black; */
}

.up_name {
  position: absolute;
  left: 60px;
  width: 200px;
  font-size: 16px;
  /* border: 1px solid black; */
  color: #f46200;
}
.infinite-list-wrapper {
  height: 800px;
  width: 1000px;
  text-align: left;
  position: relative;
  left: 20%;
  /* border: 1px solid black; */
}
.infinite-list-wrapper .list {
  padding: 0;
  margin: 0;
  list-style: none;
}
/* 滚动条 */
.infinite-list-wrapper::-webkit-scrollbar {
  width: 0 !important;
}

.infinite-list-wrapper .list-item {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 50px;
  background: var(--el-color-danger-light-9);
  color: var(--el-color-danger);
}
.infinite-list-wrapper .list-item + .list-item {
  margin-top: 10px;
}
</style>
<!--<template>
  <meta name="referrer" content="no-referrer" />
  <div v-if="true" class="bili_dy">
     <h1 style="text-align: center">b站动态</h1> 
    <ul v-infinite-scroll="load" :infinite-scroll-immediate="false">
      <el-space direction="vertical" v-for="i in count" :key="i">
        <div class="dyna_body" v-if="true">
          <div class="dy_card_head">
            <div class="up_face">
              <el-avatar :size="50" :src="tbili_data.up_face_url" />
            </div>
            <div class="up_name">{{ tbili_data.up_name }}</div>
            <div class="dy_time">{{ tbili_data.post_time }}</div>
          </div>

          <div class="dy_content">
            {{ tbili_data.content }}
            <div class="bili_img_div" v-if="tbili_data.type == 1">
              <el-image
                v-for="(i, key) in tbili_data.pic_urls.length"
                :key="key"
                style="width: 103px; height: 104px"
                :src="tbili_data.pic_urls[i - 1]"
                :fit="cover"
                :preview-src-list="tbili_data.pic_urls"
                :initial-index="i - 1"
              />
            </div>
            <div
              class="bili_video"
              @click="goto_bili_video(tbili_data.video_url)"
              v-if="tbili_data.type == 2"
            >
              <div class="video_pic">
                <el-image :src="tbili_data.video_pic_url" :fit="contain" />
              </div>
              <div
                class="video_title"
                v-text="get_title(tbili_data.video_title)"
              ></div>
              <div
                class="video_desc"
                v-text="get_desc(tbili_data.video_desc)"
              ></div>
            </div>
          </div>
          <div class="dy_tail">
            <img class="share_img" src="../static/share.png" />
            {{ tbili_data.share }}
            <img class="comment_img" src="../static/comment.png" />
            {{ tbili_data.comment }}
            <img class="like_img" src="../static/like.png" />
            {{ tbili_data.like }}--{{ i }}
          </div>
        </div>
      </el-space>
    </ul>
    <p v-if="loading">Loading...</p>
    <p v-if="noMore">No more</p>
  </div>
</template>-->