class LogsController < ApplicationController

  def index
  	@logs = Log.all
  	#render json:@logs
  end

  def new
  	@log = Log.new
  end

  def create
  	if Log.create(safe_params)
  		flash["bg-success".to_sym] = "Thank you for taking our survey"
  		redirect_to '/'
  	else
  		redirect_to '/path'
  	end
  end

  def safe_params
  	params.require(:log).permit(:q1, :q2, :q3, :q4, :q5, :q6)
  end
end
