<template>
  <div>
    <el-date-picker
      v-model="value"
      type="datetimerange"
      :picker-options="pickerOptions"
      range-separator="至"
      start-placeholder="开始日期"
      end-placeholder="结束日期"
      align="right"
      :default-time="['00:00:00']"
    >
    </el-date-picker>
  </div>
</template>

<script>
  function pickDateRangeToNow(picker, timeBefore) {
    const end = new Date();
    const start = new Date();
    start.setTime(start.getTime() - timeBefore);
    picker.$emit('pick', [start, end]);
  }
  export default {
    name: 'TimePicker',
    data() {
      return {
        value: '',
        pickerOptions: {
          shortcuts: [
            {
              text: '最近一小时',
              onClick(picker) {
                pickDateRangeToNow(picker, 3600 * 1000);
              },
            },
            {
              text: '最近一周',
              onClick(picker) {
                pickDateRangeToNow(picker, 3600 * 1000 * 24 * 7);
              },
            },
            {
              text: '最近一个月',
              onClick(picker) {
                pickDateRangeToNow(picker, 3600 * 1000 * 24 * 30);
              },
            },
            {
              text: '最近三个月',
              onClick(picker) {
                pickDateRangeToNow(picker, 3600 * 1000 * 24 * 90);
              },
            },
          ],
        },
      };
    },
    methods: {},
  };
</script>

<style lang="scss" scoped></style>
