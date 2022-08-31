// 引入node上传模块
import {Promise as router} from "q";

var multer = require('multer');

// 配置存储路径 和 重命名
var storage = multer.diskStorage({
  // 图片上传到服务器以后 要放置的路径
  destination: 'public/upload',

  // 图片重命名
  filename: function (req, file, cb) {
    var fileFormat = (file.originalname).split(".");
    // 获取时间戳
    var filename = new Date().getTime();
    // 124354654 + "." + jpg
    cb(null, filename + "." + fileFormat[fileFormat.length - 1]);
  }
});

// 上传对象
var upload = multer({
  storage,
});

// 接收上传请求
router.post('/uploadavatar', upload.single('file'), (req, res) => {
  // 接收到的文件信息
  var file = req.file;
  console.log(file)

  // 文件名
  let fileName = file.filename;
  // 拼接文件路径
  let avatarUrl = '/upload/' + fileName

  // 构造sql
  const sqlStr = `update accounts set avatarUrl = '${avatarUrl}' where id=${req.user.id}`;
  // 执行sql
  connection.query(sqlStr, (err, data) => {
    if (err) throw err;
    if (data.affectedRows > 0) {
      res.send({code: 0, reason: "上传成功", avatarUrl})
    } else {
      res.send({code: 1, reason: "上传失败"})
    }
  })
})
export default {
  upload
}
