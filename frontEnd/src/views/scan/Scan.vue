<template>
<div>
    <a-upload
        name="avatar"
        listType="picture-card"
        class="avatar-uploader"
        :showUploadList="false"
        :customRequest="selfUpload"
        :beforeUpload="beforeUpload"
        ref="upload"
        :disabled="!canClick"
    >
        <img v-if="imageUrl" :src="imageUrl" alt="avatar" style="height: 800px;width: 400px;" @click="showImgShade"/>
        <div v-else>
            <a-icon type="plus" />
            <div class="ant-upload-text" >添加图片</div>
        </div>
        <span class="delete-img" @click="deleteImg" v-if="imageUrl">x</span>
    </a-upload>
    <div class="img-shade" ref="imgShade">
        <a-icon type="close" class="close-img-shade" @click="closeImgShade"/>
        <img :src="imageUrl" class="box">
    </div>
</div>
</template>
<script>
import { ocr } from '@/api/index';
export default {
    data () {
        return {
            imageUrl: '',
            canClick: true,
        }
    },
    methods: {
        showImgShade() {
            this.$refs.imgShade.style.display = "block";
        },
        closeImgShade() {
            this.$refs.imgShade.style.display = "none";
        },
        deleteImg(e) {
            this.canClick = true;
            this.imageUrl = '';
            e.stopPropagation();
        },
        getBase64 (img, callback) {
            const reader = new FileReader()
            reader.addEventListener('load', () => callback(reader.result))
            reader.readAsDataURL(img)
        },
        selfUpload({ action, file, onSuccess, onError, onProgress }) {
            const base64 = new Promise(resolve => {
                const fileReader = new FileReader();
                fileReader.readAsDataURL(file);
                fileReader.onload = () => {
                    resolve(fileReader.result);
                    let params = {
                        img:this.imageUrl
                    };
                    ocr(params).then((res)=>{
                        this.$router.push('#/account/consumption');
                    });
                    this.imageUrl = fileReader.result;
                    this.canClick = false;
                };
            });
            console.log(this.imageUrl);
        },
        beforeUpload (file) {
            const isJPG = file.type === 'image/jpeg' || file.type === 'image/jpg' || file.type === 'image/png' || file.type === 'image/bmp' 
            if (!isJPG) {
                this.$message.error('请上传图片文件');
            }
            const isLt2M = file.size / 1024 < 200 && file.size / 1024 > 10;
            if (!isLt2M) {
                this.$message.error('文件大小应在10KB~20KB之间');
            }
            return isJPG && isLt2M
        },
    },
    mounted() {
        this.$nextTick(function() {
            this.$refs.upload.$el.childNodes[0].style.width = "116px";
            this.$refs.upload.$el.childNodes[0].style.height = "156px";
            this.$refs.upload.$el.childNodes[0].style.position = "relative";
        })
    } 
};
</script>
<style scoped>
.avatar-uploader > .ant-upload {
    width: 128px;
    height: 128px;
}
.ant-upload-select-picture-card i {
    font-size: 32px;
    color: #999;
}

.ant-upload-select-picture-card .ant-upload-text {
    margin-top: 8px;
    color: #666;
}
.delete-img {
    display: inline-block;
    position: absolute;
    left: 100%;
    top: 0;
    font-size: 40px;
}
.delete-img:hover {
    color: #FFF;
}
.img-shade {
    position: fixed;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: none;
}
.img-shade .box {
    display: block;
    margin: 50px auto;
    max-width: 400px;
    max-height: 560px;
}
.close-img-shade {
    color: #FFF;
    position: absolute;
    font-size: 30px;
    top: 20%;
    right: 20%;
    cursor: pointer;
}
</style>

