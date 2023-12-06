<script lang="ts" setup>
import { NButton, NCard, NTabs, NTabPane, NForm, NFormItemRow, NInput, FormInst, useMessage, NIcon } from 'naive-ui'
import { useRouter } from 'vue-router'
import { ref } from 'vue'
import { fetchLogin, fetchRegister } from '@/api'
import { GlassesOutline, Glasses } from '@vicons/ionicons5'
import { useUserStore } from '@/store'
// import { ChatLayout } from '../chat/layout'

const router = useRouter()
const message = useMessage()

const userStore = useUserStore()


function goHome() {
    router.push('/chat')
}

const loginFormRef = ref<FormInst | null>(null)
const registerFormRef = ref<FormInst | null>(null)

const loginFormValue = ref({
    username: '',
    password: ''
})
const registerFormValue = ref({
    username: '',
    password: '',
    nickname: ''
})
const reenteredPassword = ref<string>()

const rules = {
    username: {
        required: true,
        message: 'Please input your username',
        trigger: 'blur'
    },
    password: {
        required: true,
        message: 'Please input your password',
        trigger: ['input', 'blur']
    }
}

function handleLoginClick(e: MouseEvent) {
    e.preventDefault()
    if (loginFormValue.value.username == "" || loginFormValue.value.password == "") {
        message.error("用户名或密码不能为空")
    } else {
        loginFormRef.value?.validate((errors) => {
            if (!errors) {
                //post request
                const res = fetchLogin<Chat.LoginRequest>(loginFormValue.value.username, loginFormValue.value.password)
                res.then( response => {
                    if (response.message == '登录成功') {
                        message.success('登录成功')
                        console.log(response)
                        userStore.userInfo.name = response.data.nickname
                        goHome()
                    } else if (response.message == '用户名或密码错误') {
                        message.error('用户名或密码错误')
                    }
                }).catch(error => {
                    console.log(error)
                    message.error('后端系统错误')
                })
            } else {
                message.error('用户名和密码格式不正确')
            }
        })
    }
}

function handleRegisterClick(e: MouseEvent) {
    e.preventDefault()
    console.log(registerFormValue.value)
    if (registerFormValue.value.password != reenteredPassword.value) {
        message.error('两次输入密码不一致')
    } else if (registerFormValue.value.username == "" || registerFormValue.value.password == "") {
        message.error('用户名或密码不能为空')
    } else {
        registerFormRef.value?.validate((errors) => {
            if (!errors) {
                //post request
                const res = fetchRegister(registerFormValue.value.username, registerFormValue.value.password, registerFormValue.value.nickname)
                res.then(response => {
                    if (response.message == '注册成功') {
                        message.success('注册成功')
                    } else if (response.message == '用户已注册') {
                        message.error('用户已注册')
                    }
                }).catch(error => {
                    console.log(error)
                    message.error('后端系统错误')
                })
            } else {
                message.error('用户名和密码格式不正确')
            }
        })
    }


}

</script>

<template>
    <div class="flex h-full justify-center items-center">
        <n-card style="width:500px">
            <n-tabs class="card-tabs" default-value="signin" size="large" animated style="margin: 0 -4px"
                pane-style="padding-left: 4px; padding-right: 4px; box-sizing: border-box;">
                <n-tab-pane name="signin" tab="登录">
                    <n-form ref="loginFormRef" :rules="rules" :model="loginFormValue">
                        <n-form-item-row label="用户名">
                            <n-input v-model:value="loginFormValue.username" :maxlength="8" />
                        </n-form-item-row>
                        <n-form-item-row label="密码">
                            <n-input type="password" v-model:value="loginFormValue.password" show-password-on="mousedown"
                                :maxlength="8" />
                            <template #password-visible-icon>
                                <n-icon :size="16" :component="GlassesOutline" />
                            </template>
                            <template #password-invisible-icon>
                                <n-icon :size="16" :component="Glasses" />
                            </template>
                        </n-form-item-row>
                    </n-form>
                    <n-button type="primary" block secondary strong @click="handleLoginClick">
                        登录
                    </n-button>
                </n-tab-pane>
                <n-tab-pane name="signup" tab="注册">
                    <n-form ref="registerFormRef" :rules="rules" :model="registerFormValue">
                        <n-form-item-row label="用户名">
                            <n-input v-model:value="registerFormValue.username" :maxlength="8" />
                        </n-form-item-row>
                        <n-form-item-row label="昵称">
                            <n-input v-model:value="registerFormValue.nickname" :maxlength="20" />
                        </n-form-item-row>
                        <n-form-item-row label="密码">
                            <n-input type="password" v-model:value="registerFormValue.password" show-password-on="mousedown"
                                :maxlength="8" />
                            <template #password-visible-icon>
                                <n-icon :size="16" :component="GlassesOutline" />
                            </template>
                            <template #password-invisible-icon>
                                <n-icon :size="16" :component="Glasses" />
                            </template>
                        </n-form-item-row>
                        <n-form-item-row label="重复密码">
                            <n-input type="password" v-model:value="reenteredPassword" show-password-on="mousedown"
                                :maxlength="8" />
                            <template #password-visible-icon>
                                <n-icon :size="16" :component="GlassesOutline" />
                            </template>
                            <template #password-invisible-icon>
                                <n-icon :size="16" :component="Glasses" />
                            </template>
                        </n-form-item-row>
                    </n-form>
                    <n-button type="primary" block secondary strong @click="handleRegisterClick">
                        注册
                    </n-button>
                </n-tab-pane>
            </n-tabs>
        </n-card>
    </div>
</template>
  
<style scoped>
.card-tabs .n-tabs-nav--bar-type {
    padding-left: 4px;
}
</style>
