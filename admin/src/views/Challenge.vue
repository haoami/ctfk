<template>
  <div id="challenges">
    <div style="height: auto;" class="container">
      <div class="title">
        <h2><i :class="'el-icon-'+challenges[challengeType]" style="margin-right: 10px;" />{{challengeType}}</h2>
        <el-divider content-position="right">
        </el-divider>
      </div>
      <el-tabs tab-position="left" style="height: 100%;" v-model="challengeType">
        <el-tab-pane :name="name" v-for="(icon, name) in challenges" :key="name">
          <span slot="label"><i :class="'el-icon-'+icon" style="margin-right: 2px;" />{{name}}</span>
        </el-tab-pane>
        <challenge :type="challengeType" style="min-height: 400px" v-if="reload"></challenge>
      </el-tabs>
    </div>
  </div>
</template>

<script>
  import {AddChallengeAPI} from '@/api/auth'
  import Challenge from './compoents/challenge'

  export default {
    components: {
      Challenge: Challenge,
    },
    name: "challenges",
    data: () => {
      return {
        reload: true,
        user: {},
        challengeType: 'Pwn',
        challenges: {
          "Android": "mobile-phone",
          "Crypto": "lock",
          "Misc": "connection",
          "Pwn": "cpu",
          "Reverse": "refresh",
          "Web": "monitor"
        },
        // 表单value
        showDialog: false,
        title: '',
        type: '',
        flag: '',
        des: '',
        score: 500
      }
    },
    methods: {
      handleClose: function() {
        this.$confirm('此操作将不会放弃当前已编辑内容!!!', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.showDialog = false;
          this.$message({
            type: 'info',
            message: '放弃添加题目!'
          });
        })
      },
      ReloadSelf: function() {
        this.reload = false;
        this.$nextTick(() => {
          this.reload = true
        })
      }
    },
    watch: {
      $route: function(to, from) {
        if (to.path === '/challenges') {
          //重新渲染子组件
          this.ReloadSelf();
        }
      }
    },
  }
</script>

<style scoped>

  .container {
    text-align: center;
    margin: 0 auto;
    /* 		margin-right: 16%; */
    max-width: 100%;
  }
  .title {
    margin: 0 auto;
    max-width: 65%;
  }
  .el-dialog{
    width: 80%;
    height: 80%;
    background: green;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
  }
  .el-dialog .el-dialog__body{
    width: 60%;
    height: 60%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>
