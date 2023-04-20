<template>
  <el-button
    type="primary"
    id="dynasicShow"
    @click="gotoDynasic"
    v-text="buttonTip"
  ></el-button>
  <el-button
    type="primary"
    id="personShow"
    @click="gotoPerson"
    v-if="buttonTip == '动态'"
    >个人中心</el-button
  >
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
    <el-carousel-item v-for="item in 3" :key="item">
      <div
        class="infinite-list-wrapper"
        style="overflow: auto"
        v-if="item == 1"
      >
        <h1 style="text-align: center" v-if="item == 1">知乎热榜</h1>
        <ul v-infinite-scroll="load" :infinite-scroll-immediate="false">
          <el-space
            direction="vertical"
            v-for="(n, i) in nzhihu_data.length"
            :key="i"
          >
            <el-card
              class="zhcard"
              :body-style="{ width: '800px', height: '60px' }"
              @click="gotoZhihu(i)"
            >
              <div class="tagtest">
                <el-tag :size="20">{{ nzhihu_data[i].Z_item_rank }}</el-tag>
              </div>
              <div class="title">{{ nzhihu_data[i].Z_item_name }}</div>
              <svg
                width="18"
                height="18"
                viewBox="0 0 24 24"
                data-new-api="FireFill24"
                data-old-api="FireFill24"
                class="zhihu_hot_img"
                fill="currentColor"
              >
                <path
                  d="M14.602 21.118a8.89 8.89 0 003.72-2.232 8.85 8.85 0 002.618-6.31c0-.928-.14-1.836-.418-2.697a8.093 8.093 0 00-1.204-2.356s.025.035-.045-.055-.1-.115-.1-.115c-.955-1.078-1.504-1.984-1.726-2.854-.06-.232-.138-.88-.22-1.824L17.171 2l-.681.02c-.654.018-1.089.049-1.366.096a7.212 7.212 0 00-3.77 1.863 6.728 6.728 0 00-1.993 3.544l-.088.431-.182-.4a5.032 5.032 0 01-.326-.946 71.054 71.054 0 01-.204-.916l-.199-.909-.833.42c-.52.263-.862.462-1.076.624a8.588 8.588 0 00-2.5 2.976 8.211 8.211 0 00-.888 3.723 8.93 8.93 0 002.616 6.35 8.87 8.87 0 003.093 2.027c-.919-.74-1.593-1.799-1.76-3.051-.186-.703.05-2.352.849-2.79 0 1.938 2.202 3.198 4.131 2.62 2.07-.62 3.07-2.182 2.773-5.688 1.245 1.402 1.65 2.562 1.838 3.264.603 2.269-.357 4.606-2.003 5.86z"
                  fill-rule="evenodd"
                  clip-rule="evenodd"
                ></path>
              </svg>
              <p class="zhihu_hot">{{ nzhihu_data[i].Z_item_hot }}</p>
              <div class="zh_img">
                <el-image
                  :src="nzhihu_data[i].Z_item_cover_url"
                  :fit="contain"
                />
              </div>
            </el-card>
          </el-space>
        </ul>
      </div>
      <div
        class="infinite-list-wrapper"
        style="overflow: auto"
        v-if="item == 2"
      >
        <h1 style="text-align: center">微博热榜</h1>
        <ul v-infinite-scroll="load" :infinite-scroll-immediate="false">
          <el-space
            direction="vertical"
            v-for="(n, i) in nweibo_data.length"
            :key="i"
          >
            <el-card
              class="wb_card"
              :body-style="{ width: '800px', height: '20px' }"
              @click="goto_wb(i)"
            >
              <div class="tagtest">
                <el-tag :size="20">{{ nweibo_data[i].Weibo_item_rank }}</el-tag>
              </div>
              <div class="title">{{ nweibo_data[i].Weibo_item_name }}</div>
              <div class="weibo_hot">{{ nweibo_data[i].Weibo_item_hot }}</div>
              <el-icon :size="25" class="wb_right_arrow"
                ><arrow-right
              /></el-icon>
            </el-card>
          </el-space>
        </ul>
      </div>
      <div
        class="infinite-list-wrapper"
        style="overflow: auto"
        v-if="item == 3"
      >
        <h1 style="text-align: center">b站热榜</h1>
        <ul v-infinite-scroll="load" :infinite-scroll-immediate="false">
          <el-space
            direction="vertical"
            v-for="(n, i) in nbili_data.length"
            :key="i"
          >
            <el-card
              class="wb_card"
              :body-style="{ width: '800px', height: '80px' }"
              @click="goto_bili(i)"
            >
              <div class="bili_title">{{ nbili_data[i].Bili_item_name }}</div>
              <img
                class="bili_view_img"
                data-v-0c3f5fbc=""
                src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAC60lEQVR4Xu2aMYgTQRSG31sCprBXRMHmbIRT0EZrweau9ArhrtuZ2QTS2YidrYUEYjKznZc0Z3daHCpYnFrdgYogouAVeiDYaZFAdp6suLDuJdnsXWJ2M5Muu28n7//mzcubnYdg+AcN1w8WgI0AwwnYJWB4ANgkONYSqNfrx8rl8orWehERFwHgAgCcyFP0IOI+Ee0i4lsi+tDv9zer1eqvNB9TAbRarQVEfAAA19IGy9n9N4hYZYy9HuXXSABKqSUiepwzYZncQUSPMdYa9tBQAEopQUTNTL+WU2NEXGaMPRnk3kAASqmrRPRqwAMKEV8GQbDted5envT6vn9aa30FAJYBYDXpGxGdE0J8Sl4/AKDRaBwvlUrbAHAxbuw4zmXXdXfzJHqYL1LKGwCwkbj/vNfrLdVqtV78+gEAUsqbANBJPLzCOX9UBPGRj77vX9Ja7/wjFnGNMbY+EoBS6i4R3YkZrXPO14okPvJVSikBgEXfieieEOJWWgRs/l1HkV3hZj9yXCm1SkQPY4Kfcs6vp0XANyI6FRk5jnPGdd2vRYyAZrN51nGcLzHfv3POT6ZFAMUNOOepxVKe4UgpR+oZlAQtABsBMQJ2CdgccLQkGFZliHifiPYQcYOIOpzzH/8rcc48CSql3hPR+ZjgfQBoB0HQqVQq76YNYuYAkg4kBLfDiBBCbE0LRN4BRLpfIGK72+12kpuVo4IpCoA/Oonoo+M4bUTsuK4br+AOzaFQAGIqf4Z5Qmvd8Txv0HuJsYEUFUBcYLg5ax92Oz4PACIYO0R0WwjxbOzpB4B5AhDq/sw5X7AAMhCYpwgwdgkYmQTN/Bs0uRAythSe/82Q3Q6b/kIkQ80yFdOZF0JTUZVhUAvAHozYk6FsR2NKKeMPR40/Hje+QcLsFhnjm6TCGsPoNrmoyDK6UTIGwdxW2QiC0c3SEQSj2+UzbLwKaVroFrhJELcAJkGxyGPYCCjy7E3CdxsBk6BY5DF+A1q1ml9Q5ZM4AAAAAElFTkSuQmCC"
                alt="play"
              />
              <div class="bili_view">
                {{ nbili_data[i].Bili_item_view }}
              </div>
              <img
                class="bili_danmu_img"
                data-v-0c3f5fbc=""
                src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAADIklEQVR4Xu1aPYgTQRR+bxPwCntFFGy0PAUrrYVY3IEIHiieJ2hmdgiks7OztQrEzUzwhxMVtFBOGw8bObRS0MrCQgsVrrcJJPMkcgubTbKT3M3gLjspd2bffO/Le9/uYz+Ekv+w5PmDJ8BXQMkZ8C1Q8gLwIjhTC7RarX0LCwsrWutFRFwEgBMAcCBP1YOIv4noEyJ+IaKv/X5/o9Fo/DFhNBLQ6XSOIeJdADhrCpaz9c+I2GCMfcjClUmAUmqJiF7lLLG54CCiYIx1pt00lQClVEhE0Vyn5XQzIi4zxl5PgjeRAKXUGSJ6n76BiO4FQfBuMBhsCSF+5Cnfbrd7WGt9GgCWAWB1AvbjYRh+S18fI6Ddbu+vVqtbAHAysXlba70mhHiTp6SnYZFSXgSAZ6n1t71eb6nZbPaS18cIkFJeBoDHI5sQrzDGRq7lnYhut3tKa/0xlcdVxtijTAKUUreJ6Fa8CRHXGWNreU94Ej4ppQQAFq8R0Z0wDG+aKmBjp4/+7dNaXxBCvCgiAUqpVSJaT2Df5JzXTBXwi4gOxZs458Z3hbySE0XR0SAIvie1jHN+0FQBlNxQZAKGeUgpM/OZJIKeAF8BCQZ8CxRYBL0GuBZBk8Km120/LmdpTxPGPT0FTME9AalnsK8Aywz89xawnI+TcKY23ZMGOEFsOagnwM8Cfhjy02DWcOdFMC26JtW0LNLOw5nysVoBpsNcvRpnvRCZMHkCbLaAiW1fAY6Go9y0gHNF28UBpqq0qgG7wOf8Fk+AnwX8LOBngblmAaXUyMfRIAiO1Ov1n87VytEBKRHcnuXj6MjncQBY4Zw/d4TPadgoiq4FQfBg3s/jIwaJoS8oDMMbTpE6Cq6UekJEl+LwsxokxiwyWutzRfEHxclKKc8DwIixAxHNFplJJqkdF2aDc/7S0Z9lNWwURbVKpXI/afQAgNlMUkMk02xyiPh0MBhsCiEeWkVsIVhskyOiGiJeT4ckotlscvGNpTZKJkgor1U2JqHUZumYhFLb5S3oU65DFNYDaItVT4AtJosax1dAUf85W7h9Bdhisqhx/gL/0kVfsTNufQAAAABJRU5ErkJggg=="
                alt="like"
              />
              <div class="bili_danmu">
                {{ nbili_data[i].Bili_item_comment }}
              </div>
              <div class="bili_img">
                <el-image
                  :src="nbili_data[i].Bili_item_cover_url"
                  :fit="contain"
                />
              </div>
              <el-icon :size="45" class="bili_right_arrow"
                ><arrow-right
              /></el-icon>
            </el-card>
          </el-space>
        </ul>
      </div>
    </el-carousel-item>
  </el-carousel>
</template>

<script lang="ts" setup>
import { el } from "element-plus/lib/locale";
import { ArrowRight } from "@element-plus/icons";
import { ArrowLeftBold } from "@element-plus/icons";
import { computed, ref } from "vue";
const count = ref(20);
const loading = ref(false);
const kong = true;
const noMore = computed(() => count.value >= 36);
// const nzhihu_data = ref("2333333");
// const get_nzhihu_data = () => {
//   axios
//     .get("http://127.0.0.1:8000/api/zhihu/hot_item")
//     .then((response) => {
//       // handle response
//       nzhihu_data.value = response.data;
//       console.log("查询ing");
//     })
//     .catch((error) => {
//       console.log(error);
//     });
// };
// const load = () => {
//   if (count.value < 32) {
//     loading.value = true;
//     setTimeout(() => {
//       count.value += 2;
//       loading.value = false;
//     }, 100);
//   } else {
//     loading.value = false;
//   }
// };
</script>
<script lang="ts">
import axios from "axios";
import qs from "qs";
axios.defaults.withCredentials = true;
import { useRouter } from "vue-router";
export default {
  data() {
    return {
      isRoot: false,
      buttonTip: "",
      nzhihu_data: {},
      nweibo_data: {},
      nbili_data: {},
      zhihu_data: {
        hot: "2508 万",
        img_url:
          "https://pica.zhimg.com/80/v2-2ea663d8f92fb97cd2d63d7850063376_720w.jpg?source=1940ef5c",
        rank: "1",
        title: "怎样看待吉林农业科技学院发生的疫情以及校领导被免职？",
        title_url: "https://www.zhihu.com/question/521166378",
      },
      weibo_data: {
        hot: "3659081",
        rank: "1",
        title: "第二部黑匣子画面",
        title_url:
          "https://s.weibo.com/weibo?q=%23%E7%AC%AC%E4%BA%8C%E9%83%A8%E9%BB%91%E5%8C%A3%E5%AD%90%E7%94%BB%E9%9D%A2%23&Refer=top",
      },
      bili_data: {
        danmu: 5053,
        desc: "你们这个魔法学校，麻瓜能上吗",
        pic_url:
          // "https://pica.zhimg.com/80/v2-2ea663d8f92fb97cd2d63d7850063376_720w.jpg?source=1940ef5c",
          "http://i2.hdslb.com/bfs/archive/654ad85349714a5b79ec69b83e2e3663353f7f11.jpg",
        title: "【STN快报第六季26】lol电竞经理有钱就能当？",
        up: "STN工作室",
        video_url: "https://b23.tv/BV1a34y147Gc",
        view: 345925,
      },
    };
  },

  methods: {
    gotoManage() {
      window.open("http://127.0.0.1:8080/manage", "_self");
    },
    gotoPerson() {
      window.open("http://127.0.0.1:8080/person", "_self");
    },
    gotoDynasic() {
      window.open("http://127.0.0.1:8080/dynasic", "_self");
    },
    gotoZhihu(i) {
      window.open(this.nzhihu_data[i].Z_item_url);
      // window.location.href = this.nzhihu_data[i].Z_item_url;
    },
    goto_wb(i) {
      window.open(this.nweibo_data[i].Weibo_item_url);
    },
    goto_bili(i) {
      window.open(this.nbili_data[i].Bili_item_url);
    },
  },

  created() {
    axios.get("http://127.0.0.1:8000/api/isRoot").then((response) => {
      this.isRoot = response.data.status;
    });
    if (localStorage.userName) {
      this.buttonTip = "动态";
    } else {
      this.buttonTip = "登陆";
    }
    axios
      .get("http://127.0.0.1:8000/api/zhihu/hot_item")
      .then((response) => {
        // handle response
        this.nzhihu_data = response.data;
        console.log("查询ing");
      })
      .catch((error) => {
        console.log(error);
      });
    axios
      .get("http://127.0.0.1:8000/api/weibo/hot_item")
      .then((response) => {
        // handle response
        this.nweibo_data = response.data;
        console.log("查询ing");
      })
      .catch((error) => {
        console.log(error);
      });
    axios
      .get("http://127.0.0.1:8000/api/bili/hot_item")
      .then((response) => {
        // handle response
        this.nbili_data = response.data;
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
#personShow {
  position: fixed;
  right: 30px;
  top: 10px;
  z-index: 1;
  height: 40px;
  width: 120px;
}

#dynasicShow {
  position: fixed;
  left: 30px;
  top: 10px;
  z-index: 1;
  height: 40px;
  width: 120px;
}
.bili_right_arrow {
  position: absolute;
  right: -750px;
  top: 20px;
}
.bili_view_img {
  position: absolute;
  left: 210px;
  bottom: 10px;
  width: 20px;
}
.bili_view {
  position: absolute;
  left: 230px;
  bottom: 10px;
  /* border: 2px solid blue; */
  display: inline;
  font-size: 13px;
  color: #999;
}

.bili_danmu_img {
  position: absolute;
  left: 310px;
  bottom: 10px;
  width: 20px;
}

.bili_danmu {
  position: absolute;
  left: 330px;
  bottom: 10px;
  /* border: 2px solid blue; */
  display: inline;
  font-size: 13px;
  color: #999;
}

.bili_img {
  position: absolute;
  left: 20px;
  top: 10px;
  width: 150px;
  height: 80px;
  /* border: 2px solid green; */
}
.bili_title {
  position: absolute;
  left: 200px;
  width: 450px;
  display: inline;
  /* border: 2px solid black; */
  margin: 0 8px;
  text-align: left;
}
.wb_card {
  position: relative;
  left: 0%;
}
.wb_right_arrow {
  position: relative;
  right: -750px;
}
.weibo_hot {
  position: absolute;
  right: 100px;
  /* border: 2px solid blue; */
  display: inline;
  font-size: 13px;
  color: #999;
}

.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 150px;
  margin: 0;
  text-align: center;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}

#ArrowRight {
  position: fixed;
  top: 40%;
  right: 20px;
}

#ArrowLeft {
  position: fixed;
  top: 40%;
  left: 20px;
}

.zhcard {
  position: relative;
  left: 0%;
}
.zh_img {
  position: absolute;
  right: 20px;
  top: 10px;
  width: 150px;
  height: 80px;
  /* border: 2px solid green; */
}
.tagtest {
  position: absolute;
  left: 0px;
  display: inline;
  /* border: 2px solid red; */
  margin: 0 8px;

  /* margin-top: 13px; */
  /* line-height: 12px; */
}
.title {
  position: absolute;
  left: 50px;
  width: 450px;
  display: inline;
  /* border: 2px solid black; */
  margin: 0 8px;
  text-align: left;
}
.zhihu_hot_img {
  position: absolute;
  left: 60px;
  bottom: 17px;
}

.zhihu_hot {
  position: absolute;
  left: 80px;
  bottom: 2px;
  font-size: 13px;
  color: #999;
  display: inline;
  /* border: 2px solid yellow; */
}

.bottom {
  position: absolute;

  margin-top: 13px;
  line-height: 12px;
  width: 550px;
  height: 12px;
  /* display: flex; */
  /* justify-content: space-between;
  align-items: center; */
  /* border: 2px solid red; */
}

.button {
  padding: 0;
  min-height: auto;
}

.image {
  width: 100%;
  display: block;
}

/*  */
.infinite-list-wrapper {
  height: 800px;
  width: 1100px;
  text-align: center;
  position: relative;
  left: 20%;
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


    <!-- <el-carousel trigger="click" height="790px" indicator-position="outside" :autoplay=false>
      <el-carousel-item v-for="item in 3" :key="item">
        <h3 class="small" v-if="item!=1">{{ item }}</h3>
        <h1 style="text-align: center" v-if="item==1">知乎热榜</h1>
  <div class="infinite-list-wrapper" style="overflow: auto" v-if="item==1">
    <ul  v-infinite-scroll="load"  :infinite-scroll-immediate="false" >
      <el-space direction="vertical"   v-for="i in count" :key="i">
      <el-card class="zhcard" :body-style="{ width:'800px',height:'60px' }" @click="gotoZhihu">
        <div  class="tagtest"><el-tag :size="20">{{i}}</el-tag></div>
          <div class = "title">{{ zhihu_data.title }}</div>
            <p class="hot">{{ zhihu_data.hot }}</p>
          <div class="zh_img">
        <el-image :src="zhihu_data.img_url" :fit="contain" />
          </div>
      </el-card>
      </el-space>
    </ul>
    <p v-if="loading">Loading...</p>
    <p v-if="noMore">No more</p>
  </div>
      </el-carousel-item>
    </el-carousel> -->