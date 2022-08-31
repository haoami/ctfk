<template>
  <div class="add_challenge" v-if="role">
      <v-form
        ref="form"
        v-model="valid"
        lazy-validation
      >
        <v-col  cols="12" sm="30" md="6">
          <v-text-field
            height="50px"
            v-model="title"
            :counter="10"
            label="Name"
            required
            placeholder="请输入题目名字"
          ></v-text-field>
        </v-col>
        <v-col  cols="12" sm="30" md="6">
          <v-select
            :items="types"
            :label="value_type ? '' : '请选择'"
            item-text="name"
            item-value="id"
            v-model="value_type"
            @change="getvalue_typeSelected(value_type)"
          ></v-select>
        </v-col>
        <v-col  cols="12" sm="30" md="6">
          <v-text-field
            v-model="flag"
            label="flag"
            required
            height="50px"
            placeholder="请输入flag"
          ></v-text-field>
        </v-col>
        <v-col  cols="12" sm="30" md="6">
          <v-text-field
            v-model="des"
            :counter="10"
            label="des"
            height="50px"
            required
            placeholder="描述"
          ></v-text-field>
        </v-col>
        <v-col  cols="12" sm="30" md="6">
          <v-text-field
            v-model="score"
            :counter="10"
            label="score"
            required
            height="50px"
            placeholder="分数"
          >
          </v-text-field>
        </v-col>

        <v-file-input
          accept="zip"
          label="File input"
          type="file"
          v-model="files"
        ></v-file-input>

        <v-btn
          :disabled="!valid"
          color="success"
          class="mr-4"
          @click="validate"
        >
          Validate
        </v-btn>

        <v-btn
          :disabled="!valid"
          color="success"
          class="mr-4"
          @click="Submit"
        >
          提交
        </v-btn>
      </v-form>
  </div>
  <div v-else>
  </div>
</template>

<script>
  import {AddChallengeAPI} from '@/api/auth'
  export default {
    name: "Add_Chanllenges",
    computed: {
      role: function() {
        return this.$store.state.user.role
      }
    },
    data: () => {
      return {
        types: [
          {
            id:"Web",
            name: "Web",
          },
          {
            id:"Crypto",
            name: "Crypto",
          },
          {
            id:"Misc",
            name: "Misc",
          },
          {
            id:"Pwn",
            name: "Pwn",
          },
          {
            id:"Reverse",
            name: "Reverse",
          },
          {
            id:"Pwn",
            name: "Pwn",
          }
        ],
        reload: true,
        files: null,
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
        value_type: '',
        flag: '',
        des: '',
        score: '',
        // files:''
      }
    },
    methods: {
      handleClose: function () {
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
      getvalue_typeSelected(val) {
        this.value_type = val;
      },
      Submit: async function () {
        if((this.title || this.type || this.des || this.score || this.flag) === ''){
          this.$message({
            title: '错误',
            message: '存在未填写内容',
            type: 'error'
          });
        }
        let formData = new FormData();
        if (this.files){
          for (let file in this.files){
            formData.append("files", file, file.name);
          }
          console.log(formData.getAll("cave"))
          console.log(this.files)
        }
        let challenge_info = {
        title: this.title,
        value_type: this.value_type,
        flag: this.flag,
        des: this.des,
        score: this.score,
        // files:this.files
        }
        const rsp = AddChallengeAPI(challenge_info);
        // console.log(rsp);
        // console.log(rsp.status);
        rsp.then(rsp =>{
           if (rsp.status == 200) {
          this.showDialog = false
          this.$message({
            title: '成功',
            message: '添加题目成功',
            type: 'success'
          });
          //重新渲染子组件
          this.ReloadSelf()
        } else {
          this.$confirm('添加题目失败', '提示', {
            confirmButtonText: '确定',
            type: 'error'
          })
        }
        });
      }
    }
  }
</script>

<style scoped>
  .v-text-field{
    min-height: 48px;
    font-size: large;
  }
</style>
