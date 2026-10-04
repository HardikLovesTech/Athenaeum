function StatCard({ Number, Label }) {
  return (
    <div className="StatCard">
      <div className="StatNumber">{Number}</div>
      <div className="StatLabel">{Label}</div>
    </div>
  );
}

export default StatCard;