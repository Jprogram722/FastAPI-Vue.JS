<template>
    <transition name="fade">
        <div class="backdrop" v-if="props.modalToggle == true" @click.self="$emit('close-modal')">
            <div class="container">
                <slot></slot>
            </div>
        </div>
    </transition>
</template>

<script>
export default {
    name: "Modal Component",
    props: ['modalToggle'],
    setup (props, context) {
        
        const defaultURL = 'http://localhost:8000/api';

        const handleSubmit = async (formInfo) => {
            try{
                await axios.post(defaultURL + '/form', formInfo);
                window.location.reload();
            }
            catch(err){
                console.log(err.message);
            }
        }

        return {handleSubmit, props}
    }
}
</script>

<style>
    .backdrop{
        width: 100%;
        height: 100%;
        position:fixed;
        background: rgba(0, 0, 0, 0.5);
    }

    .container{
        display: block;
        margin: 150px auto;
        width: min-content;
    }

    .fade-enter-from {opacity: 0;}

    .fade-enter-active {transition: all 100ms ease;}

    .fade-leave-to {opacity: 0;}

    .fade-leave-active {transition: all 100ms ease;}

</style>